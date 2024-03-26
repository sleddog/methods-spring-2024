const express = require('express');
const bodyParser = require('body-parser');
const { spawn } = require('child_process');

const app = express();
const port = 3000;

app.use(bodyParser.json());

app.get('/', (req, res) => {
    // Read palindrom html file and return to user

});

app.post('/isPalindrome', (req, res) => {
    const inputString = req.body.inputString;
    
    const pythonProcess = spawn('python', ['palindrome.py', inputString]);
    
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
