Swal.fire({
  title: 'Register',
  html:
    '<input id="swal-username" class="swal2-input" placeholder="Username">' +
    '<input id="swal-password" type="password" class="swal2-input" placeholder="Password">',
  confirmButtonText: 'Register',
  showCancelButton: true,
  preConfirm: () => {
    const username = document.getElementById('swal-username').value;
    const password = document.getElementById('swal-password').value;
    if (!username || !password) {
      Swal.showValidationMessage('Please enter both fields');
    }
    return { username, password };
  }
}).then((result) => {
  if (result.isConfirmed) {
    fetch('/register', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(result.value)
    })
    .then(res => res.json())
    .then(data => {
      if (data.user_id) {
        Swal.fire('User created!', '', 'success');
      } else {
        Swal.fire('Error', data.error || 'Unknown error', 'error');
      }
    });
  }
});
