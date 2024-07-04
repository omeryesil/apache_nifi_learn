from org.apache.nifi.processor.io import StreamCallback
from org.apache.commons.io import IOUtils
from java.nio.charset import StandardCharsets
import json

class PyStreamCallback(StreamCallback):
    def __init__(self):
        pass

    def process(self, inputStream, outputStream):
        # Read the entire flowfile content using IOUtils
        input_text = IOUtils.toString(inputStream, StandardCharsets.UTF_8)

        # Convert the content to JSON
        json_content = json.loads(input_text)

        # Get the length of the JSON array
        json_length = len(json_content)

        # Log the length of the JSON array
        print("Length of JSON array:", json_length)

        # Find the record with city "Montreal"
        record_with_montreal = next((record for record in json_content if record.get("city") == "Montreal"), None)
          
        if record_with_montreal:
            output_text = json.dumps(record_with_montreal)
            outputStream.write(output_text.encode('utf-8'))

        else:
            raise ValueError('No record found with city "Montreal"')

flowFile = session.get()
if flowFile is not None:
    flowFile = session.write(flowFile, PyStreamCallback())
    session.transfer(flowFile, REL_SUCCESS)
