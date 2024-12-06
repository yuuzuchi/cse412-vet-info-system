async function sha256(message) {
    // encode as UTF-8
    const msgBuffer = new TextEncoder().encode(message);                    
    // hash the message
    const hashBuffer = await crypto.subtle.digest('SHA-256', msgBuffer);
    // convert ArrayBuffer to Array
    const hashArray = Array.from(new Uint8Array(hashBuffer));
    // convert bytes to hex string                  
    const hashHex = hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
    return hashHex;
}

document.getElementById('loginButton').addEventListener('click', async function() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    try {
        // Hash the password
        const hashedPassword = await sha256(password);
        
        // Send POST request to login endpoint
        const response = await fetch('http://localhost:5000/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                username: username,
                password: hashedPassword
            })
        });

        if (response.redirected) {
            // If login successful, Flask will redirect us
            window.location.href = response.url;
        } else {
            const data = await response.json();
            if (data.error) {
                alert(data.error);
            }
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred during login');
    }
});

// Test login button
document.getElementById('testLoginButton').addEventListener('click', async function() {
    try {
        const response = await fetch('http://localhost:5000/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                username: 'dr.emma_vet',
                password: 'VetPass789'
            })
        });

        if (response.redirected) {
            window.location.href = response.url;
        } else {
            const data = await response.json();
            if (data.error) {
                alert(data.error);
            }
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred during test login');
    }
});

// Allow login with Enter key
document.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        document.getElementById('loginButton').click();
    }
});