SECRET_KEY='dev'
DATABASES = {
   PRODUCTION_DATABASE = {
       DATABASE_TYPE = "sqlite",
       DATABASE_URI = ('scheduler.sqlite')
   },
   ADMIN_DATABASE = {
       DATABASE_TYPE = "sqlite",
       DATABASE_URI = ('admin_panel.sqlite')
   }
}
