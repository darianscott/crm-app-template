export function initDashboard() {
  const dashboard = document.querySelector('[data-init="dashboard"]');
  if (!dashboard) return;

  initLicenseTable();
  initTrainingProgress();
  initTestimonialSections();
  initUserActivity();
  initAdminMetrics(); // only if user is admin and section visible
}
