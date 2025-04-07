# Example: File Upload Service

We start the web service from the command line:
```
$ python3 upload_service.py
```

## File Upload 

File upload to a Flask server works by receiving a **multipart/form-data request** containing the file. Flask provides the **request.files** object to handle 
uploaded files easily.

This upload process works as follows:

* **Client Sends File**: 
    The client (e.g., using `curl` or an HTML form) sends a POST request 
    with a file as part of the request body, typically encoded as 
    `multipart/form-data`.

* **Flask Receives Request**:
    * Flask automatically parses the incoming `multipart/form-data` request.
    * Uploaded files are accessible through `request.files`, a special 
        dictionary-like object where the key is the name of the `file` field 
        in the form.

* **File Validation and Processing**:
    * Flask checks if a file is present in `request.files`.
    * If the file exists, Flask allows us to save it to the server or perform 
        operations on it.

_Example:_ curls sends a file to the server:
```
$ curl -ik -X POST -F "file=@./images/tux.jpeg" https://localhost:8443/uploads

$ curl -ik --proxy http://localhost:8010 -X POST -F "file=@./images/tux.jpeg" https://localhost:8443/uploads
```

This curl command sends an HTTP POST request to `https://localhost:8443/uploads`
and includes a file (`tux.jpeg` in the `./images/` directory) in the request 
body under the form field named `file`.

* **-i**: Includes the response headers in the output. Without this option, 
    curl only shows the response body by default.

* **-k**: Insecure Mode - Skips verifying the SSL certificate of the server.
    Typically used for testing HTTPS servers with self-signed certificates.

* **-F "file=@./images/tux.jpeg"**: Specifies form data to send as part of a 
    `multipart/form-data` POST request.    
    * `file=`: Indicates the name of the form field `file`
    * `@./images/tux.jpeg`: Path to the file being uploaded (relative to the current directory).
 
* **https://localhost:8443/uploads**: The URL to which the file is uploaded.


## Server-Side Validation

On the server side, we validate the uploaded file:

* **Checking if a File was Selected**: Ensures the user has selected a file.
    If validation fails, the server responds with **HTTP 400** and a message.

    ```Python
        if file.filename == '':
            return jsonify({'message': 'No selected file'}), 400

    ```

* **File Type Validation**: Validates the file extension.
    Checks if the filename contains a dot `.`, extracts the file extension 
    (using `rsplit('.', 1)[1]` to split from the right and get the last part 
    after the dot), converts the extension to lowercase (`lower()`) and 
    checks if it exists in the `ALLOWED_EXTENSIONS` set.

    ```Python
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

    def allowed_file(filename):
        return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    ```

    ```Python
    if file and allowed_file(file.filename):
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify({'message': f'File {filename} uploaded successfully'}), 200
    ```

## Additional Server-Side Checks

* **Sanitize File Names**: Use `werkzeug.utils.secure_filename` to prevent 
    directory traversal attacks.

    ```Python
    from werkzeug.utils import secure_filename

    filename = secure_filename(file.filename)
    ```

* **Set Maximum File Size**: Prevent excessively large uploads with:

    ```Python
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB
    ```

* **Error Logging**: Log validation errors for debugging and analytics.



*Egon Teiniker, 2020-2024, GPL v3.0*