async function handleLogout() {
    try {
        const response = await fetch('/logout', {
            method: 'GET',
            credentials: 'same-origin'
        });
        
        if (response.redirected) {
            window.location.href = response.url;
        } else {
            window.location.href = '/login';
        }
    } catch (error) {
        console.error('Logout failed:', error);
        alert('Logout failed. Please try again.');
    }
}
