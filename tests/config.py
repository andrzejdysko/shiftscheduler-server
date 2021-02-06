SECRET_KEY="dev"
SCHEDULER_CONFIG={
            "PRODUCTION_DATABASE" : {
                "TYPE" : "mysql",
                "NAME" : "test_scheduler",
                "HOST": "localhost",
                "PORT":3306,
                "USER" : "scheduleruser",
                "PASSWORD" : "bM1stkriG"
            },
            "ADMIN_DATABASE" : {
                "TYPE" : "mysql",
                "NAME" : "test_dbpanel",
                "HOST": "localhost",
                "PORT":3306,
                "USER" : "scheduleruser",
                "PASSWORD" : "bM1stkriG"
            }
        }