const express = require('express');
const bodyParser = require('body-parser');
const { spawn } = require('child_process');
const path = require('path'); // Import the path module

const app = express();
const port = 3000;

app.use(bodyParser.json());

// Define a route to serve the HTML file from the frontend folder when the root URL is accessed
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, '..', 'frontend', 'palindrome.html'));
});

// Implement the POST route to handle requests from the HTML form and communicate with the Python script
app.post('/isPalindrome', (req, res) => {
    const inputString = req.body.inputString;
    
    const pythonProcess = spawn('python3', [path.join(__dirname, 'palindrome.py'), inputString]); // Use path.join to specify the correct path to the Python script
    
    let output = '';

    pythonProcess.stdout.on('data', (data) => {
        output += data.toString();
    });

    pythonProcess.on('close', (code) => {
        if (code === 0) {
            res.json({ result: output.trim() });
        } else {
            res.status(500).json({ error: 'An error occurred while executing the Python script.' });
        }
    });
});

app.listen(port, () => {
    console.log(`Server is listening at http://localhost:${port}`);
});
