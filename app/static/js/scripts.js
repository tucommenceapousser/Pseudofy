document.getElementById('pseudocodeForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    document.getElementById('loading').style.display = 'block';

    const codeInput = document.getElementById('codeInput').value;
    const languageSelect = document.getElementById('languageSelect').value;

    let attempt = 0;
    const maxAttempts = 5;
    let success = false;
    let result;

    while (attempt < maxAttempts && !success) {
        attempt++;

        try {
            const response = await fetch('/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    question: codeInput,
                    language: languageSelect
                })
            });

            result = await response.json();

            if (result.status === 'success') {
                success = true;
                document.getElementById('result').innerHTML = `<pre>${result.data}</pre>`;
            } else {
                throw new Error('Error generating pseudocode!');
            }

        } catch (error) {
            if (attempt === maxAttempts) {
                document.getElementById('result').innerHTML = 'Error processing request!';
            }
        }
    }

    document.getElementById('loading').style.display = 'none';
});
