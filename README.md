# Apache NiFi

## Launch

```shell
docker compose up
```

## Browse

[https://localhost:http://localhost:8091/nifi/](http://localhost:8091/nifi/)

## MS Sql Server Connection

Download JDBC Sql Server Driver

```shell
https://learn.microsoft.com/en-us/sql/connect/jdbc/download-microsoft-jdbc-driver-for-sql-server?view=sql-server-ver16
```

Extract:

```shell
tar -xvzf sqljdbc_12.6.2.0_enu.tar.gz
```

Copy jar to NiFi Plugins

```shell
cp sqljdbc_12.6/enu/mssql-jdbc-12.6.2.jre8.jar ./nifi/plugins/
```

Driver class name:

```text
com.microsoft.sqlserver.jdbc.SqlServerDriver


```
