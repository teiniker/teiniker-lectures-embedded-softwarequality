# Role-Based Authorization

> **Role-Based Authorization (RBA)** is a security mechanism that grants or 
> restricts access to resources and actions based on the roles assigned 
> to a user. 

This approach ensures that only authorized users with the appropriate roles 
can perform specific actions or access certain resources.

* **Roles**: A role represents a specific category of permissions or 
  responsibilities, such as Admin, Editor, Viewer, etc.
  Users are assigned one or more roles, determining what they can do within 
  the system.

* **Permissions**: Permissions define what actions (e.g., read, write, delete, 
  etc.) a user can perform or what resources they can access.
  Each role is associated with a set of permissions.


Role-Based Authorization can be implemented on different levels:

* **Method-Level Authorization**: Method-Level Authorization determines 
  whether a user can execute a specific method or action in the application 
  based on their permissions or roles. It is coarse-grained and applies to 
  an entire method, typically at the business logic or API level.

* **Object-Level Authorization**: Object-Level Authorization determines 
  whether a user can access a specific object or resource instance based 
  on their permissions. It is fine-grained and ensures users can only 
  interact with the objects they are explicitly allowed to access.

For robust security, it is often recommended to combine both methods, using 
Method-Level Authorization for broad control and Object-Level Authorization 
for granular control.


## Examples and Exercises

* **Method-Level Authorization**
  * Demo: [flask-article-service-roles](method-level/flask-article-service-roles/)

* **Object-Level Authorization**
  * Exercise: [flask-article-service-uuid](object-level/flask-article-service-uuid-exercise/) ([Model Solution](object-level/flask-article-service-uuid/))


## References
* [Flask-HTTPAuth](https://flask-httpauth.readthedocs.io/en/latest/)

*Egon Teiniker, 2020-2024, GPL v3.0*