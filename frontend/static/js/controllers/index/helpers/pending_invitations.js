export async function renderPendingInvitaionsTable(containerSelector = '#pending-invitations-table') {
    try {
        const res = await fetch('/index/helpers/pending-invitations-table');
        if (!res.ok) throw new Error('Failed to fetch pending invitations data');

        const data = await res.json();
        const container = document.querySelector(containerSelector);
        container.innerHTML = '';

        data.forEach(item => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td class="user-name">${User.userName}.userName}</td>
            <td class="invitation-sent">${User.invitationSent}</td>
            <td class="archived-invitations">${User.archivedInvitations}</td>
            <td class="reminders-sent">${User.reminderSent}</td>
            <td class="tesimonials-recieved">${User.testimonialsRecieved}</td>

        `;
        container.appendChild(row);
        });

        console.log('✅ Pending Invitation table rendered');
        } catch (err) {
        console.error('⚠️ Error rendering Pending Invitation table:', err);
        AppUtils.showToast('Pending Invitation data failed to load.');
    }
    
}
