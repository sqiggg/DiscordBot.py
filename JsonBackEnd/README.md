#Json Backend

A Json backend. Gets requests from `http://localhost:8080/json` and sends back json from the database or takes in json with a Post request and makes sure that there is no overwrite command.
If there is an overwrite command then the backend replaces the database with the Json that was sent.
