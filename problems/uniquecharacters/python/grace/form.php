<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>String Input</title>
    </head>

    <body>
        <h1>Unique Characters</h1>
        <form method="POST">
            <label for="in_string">Enter a string:</label><br>
            <input type="text" id="in_string" name="in_string"><br><br>
            <input type="submit" value="Submit">
        </form>
            <?php
                if ($_SERVER["REQUEST_METHOD"] == "POST") {
                    $inputString = $_POST["in_string"];
                    echo "Your input: " . $inputString;
                }
            ?>
        <br>
        <p>Navigation
            <ul>
                <li><a href="index.html">Back</a></li>
            </ul>
        </p>
    </body>
</html>