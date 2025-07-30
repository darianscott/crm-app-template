function buildResources() {
  const resources = {};

  document.querySelectorAll('input[type="checkbox"]:checked').forEach(cb => {
    const resourceField = cb.dataset.resource; // e.g. "user-first_name"
    const isFilterable = cb.dataset.filter === "true";

    const [model, ...fieldParts] = resourceField.split("-");
    const field = fieldParts.join("_"); // handles multi-part fields

    if (!resources[model]) {
      resources[model] = {};
    }

    resources[model][field] = isFilterable;
  });

  return resources;
}
