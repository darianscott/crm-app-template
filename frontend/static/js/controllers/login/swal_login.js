Swal.fire({
  title: 'Login',
  html:
    '<input id="swal-username" class="swal2-input" placeholder="Username">' +
    '<input id="swal-password" type="password" class="swal2-input" placeholder="Password">',
  confirmButtonText: 'Login',
  showCancelButton: true,
  preConfirm: () => {
    const username = document.getElementById('swal-username').value;
    const password = document.getElementById('swal-password').value;
    if (!username || !password) {
      Swal.showValidationMessage('Please enter both username and password');
    }
    return { username, password };
  }
}).then((result) => {
  if (result.isConfirmed) {
    fetch('/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(result.value)
    })
    .then(res => res.json())
    .then(data => {
      if (data.user_id) {
        Swal.fire('Logged in!', '', 'success');
        // Store user_id or trigger app state change
      } else {
        Swal.fire('Login failed', data.error || 'Unknown error', 'error');
      }
    });
  }
});
