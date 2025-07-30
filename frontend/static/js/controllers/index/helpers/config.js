const reportConfigs = [
  { name: 'license', payload: buildLicenseTableRequest() },
  { name: 'training-summary', payload: buildUserSummaryRequest() },
  { name: '', payload: buildComplianceReportRequest() }
];

export async function dashboardTables() {
  for (const config of reportConfigs) {
    try {
      const data = await sendReportPayload(config.payload);
      const selector = `[data-target-selector="${config.name}"]`;
      displayReport(data, selector);
    } catch (err) {
      console.error(`⚠️ Failed to render ${config.name}:`, err);
      const container = document.querySelector(`[data-target-selector="${config.name}"]`);
      if (container) container.innerHTML = `<p>Error loading ${config.name} report.</p>`;
    }
  }
}
