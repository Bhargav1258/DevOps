
# Sample REST CRUD API with Spring Boot, Mysql, JPA and Hibernate 

## Steps to Setup


**1. Create Mysql database**
```bash
create database user_database
```

**2. Change mysql username and password as per your installation**

+ open `src/main/resources/application.properties`

+ change `spring.datasource.username` and `spring.datasource.password` as per your mysql installation

**3. Build and run the app using maven**

```bash
mvn package
java -jar target/spring-boot-rest-api-tutorial-0.0.1-SNAPSHOT.jar

```

Alternatively, you can run the app without packaging it using -

```bash
mvn spring-boot:run
```

The app will start running at <http://localhost:8080>.

## Explore Rest APIs

The app defines following CRUD APIs.

    GET /api/v1/users
    
    POST /api/v1/users
    
    GET /api/v1/users/{userId}
    
    PUT /api/v1/users/{userId}
    
    DELETE /api/v1/users/{userId}



curl -X POST -H "Content-Type: application/json" --data @user.json http://localhost:8080/api/v1/users