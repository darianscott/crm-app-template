export async function renderLicenseTable(containerSelector = '#license-table') {
  try {
    const res = await fetch('/index/helpers/license-table');
    if (!res.ok) throw new Error('Failed to fetch license data');

    const data = await res.json();
    const container = document.querySelector(containerSelector);
    container.innerHTML = '';

    data.forEach(item => {
      const row = document.createElement('tr');
      row.innerHTML = `
        <td class="user-name">${License.userName}</td>
        <td class="license-type">${License.licenseType}</td>
        <td class="license-id">${License.licenseIdNumber}</td>
        <td class="expiration-date">${License.expirationDate}</td>
        <td class="days-remaining">${item.daysRemaining}</td>
        <td class="reminder-days">${License.reminderDays}</td>
        <td class="compliance-status">${License.isCompliant ? '✅' : '❌'}</td>
      `;
      container.appendChild(row);
    });

    console.log('✅ License table rendered');
  } catch (err) {
    console.error('⚠️ Error rendering license table:', err);
    AppUtils.showToast('License data failed to load.');
  }
}
