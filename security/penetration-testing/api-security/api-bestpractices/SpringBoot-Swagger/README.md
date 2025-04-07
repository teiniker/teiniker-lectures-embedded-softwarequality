# Documenting a REST API

Documentation is an essential part of building REST APIs.
**SpringDoc** is a tool that simplifies the generation and maintenance of API docs based on the 
**OpenAPI 3 specification**

## Service Setup

We use Maven to compile and run the service.
```
$ mvn spring-boot:run
```

## Access the Swagger UI

So now our API documentation will be available at:
```
https://localhost:8443/swagger-ui.html
```


## OpenAPI Specification
The **OpenAPI** descriptions will be available at the path `/v3/api-docs` by default:
```
https://localhost:8443/v3/api-docs/
https://localhost:8443/v3/api-docs.yaml
```

To use a custom path, we can indicate in the `application.properties` file:
```
springdoc.api-docs.path=/api-docs
```

## References
* [YouTube (Java Brains): How to add Swagger to Spring Boot](https://youtu.be/gduKpLW_vdY)

* [Documenting a Spring REST API Using OpenAPI 3.0](https://www.baeldung.com/spring-rest-openapi-documentation)
* [springdoc-openapi](https://springdoc.org/)

* [swagger-annotations API](https://javadoc.io/doc/io.swagger.core.v3/swagger-annotations/latest/index.html)

*Egon Teiniker, 2020-2023, GPL v3.0*