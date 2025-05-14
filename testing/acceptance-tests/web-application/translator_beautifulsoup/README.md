# Testing Web Appications Using Beautiful Soup 

## Accessing the Web Page using curl 

```Bash
$ curl -i http://localhost:8080
HTTP/1.1 200 
Vary: Origin
Vary: Access-Control-Request-Method
Vary: Access-Control-Request-Headers
Last-Modified: Fri, 14 Mar 2025 07:45:34 GMT
Accept-Ranges: bytes
Content-Type: text/html;charset=UTF-8
Content-Language: en-US
Content-Length: 1160
Date: Wed, 14 May 2025 08:05:42 GMT

<html>
<head>
    <title>Servlet Translator</title>
</head>

<body>
<h2>Translator </h2>

<form method="POST" action="translator" >
    <table border="0" >
        <colgroup>
            <col width="100"> <col width="100">
        </colgroup>
        <tr>
            <th align="left">
                Word:
            </th>
            <th align="left">
                <input type="text" name="word" maxlength="30" size="20"> <br>
            </th>
        </tr>

        <tr>
            <th align="left">
                Language
            </th>
            <th>
                <select name="language">
                    <option> Deutsch
                    <option> Francais
                </select>
            </th>
        </tr>
    </table>

    <table >
        <colgroup>
            <col width="50"> <col width="50"> <col width="50">
        </colgroup>
        <tr>
            <th>
                <input type="reset"  name="action" value="Reset">
            </th>
            <th/>
            <th>
                <input type="submit" name="action" value="Translate">
            </th>
        </tr>
    </table>
</form>
</body>
</html>
```

```Bash
$ curl -i -X POST http://localhost:8080/translator -H "Content-Type: application/x-www-form-urlencoded" -d 'word=cat&language=Deutsch&action=Translate'

HTTP/1.1 200 
Content-Type: text/html;charset=UTF-8
Content-Language: en-US
Transfer-Encoding: chunked
Date: Wed, 14 May 2025 08:12:29 GMT

<!DOCTYPE HTML>
<html>
<head>
    <title>Translation Application</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
</head>
<body>
    <h2>
        <p >Translate: cat into Katze</p>
    </h2>
    <p/>
    <a href="index.html"> back</a>
</body>
</html>
```

