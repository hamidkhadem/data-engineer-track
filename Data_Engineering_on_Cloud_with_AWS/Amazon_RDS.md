Ref: ```https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateDBInstance.html```

1. Sign in to the AWS Management Console and open the Amazon RDS console at https://console.aws.amazon.com/rds/.

2. In the upper-right corner of the Amazon RDS console, choose the AWS Region in which you want to create the DB instance.

3. In the navigation pane, choose Databases.

4. Choose Create database.

5. In Choose a database creation method, select Standard Create.

6. In Engine options, choose the engine type: MariaDB, Microsoft SQL Server, MySQL, Oracle, or PostgreSQL. Microsoft SQL Server is shown here.

7. For Version, choose the engine version.

8. In Templates, choose the template that matches your use case. If you choose Production, the following are preselected in a later step:

        a. Multi-AZ failover option

        b. Provisioned IOPS SSD (io1) storage option

        c. Enable deletion protection option

        We recommend these features for any production environment.

9. For the remaining sections, specify your DB instance settings. For information about each setting, see Settings for DB instances.

10. Choose Create database.

11. If you chose to use an automatically generated password, the View credential details button appears on the Databases page.

    To view the master user name and password for the DB instance, choose View credential details.

    To connect to the DB instance as the master user, use the user name and password that appear.

12. For Databases, choose the name of the new DB instance.

    On the RDS console, the details for the new DB instance appear. The DB instance has a status of Creating until the DB instance is created and ready for use. When the state changes to Available, you can connect to the DB instance. Depending on the DB instance class and storage allocated, it can take several minutes for the new instance to be available.

