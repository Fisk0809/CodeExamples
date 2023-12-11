const userList = document.getElementById('spillere');







function outputUsers(users) {
    userList.innerHTML = `
     ${users.map(user => `<li>${user.username}</li>`).join()}
    `;
}
