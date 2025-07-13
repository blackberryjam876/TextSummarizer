async function summarizeText() {
    const text = document.getElementById('text').value;

    const response = await fetch('/summarize', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: text })
    });

    const result = await response.json();
    document.getElementById('result').innerText = result.summary;
}
