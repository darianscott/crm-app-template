export async function askJoins(joins) {
    Swal.fire({
        title: "Join Models?",
        text: `You selected fields from ${models.length} models. Would you like to join them together?`,
        icon: "question",
        showCancelButton: true,
        confirmButtonText: "Yes, join them",
        cancelButtonText: "No"
    })(result)

    if (result.isconfimed) {
        joins = true
        return joins
    };
    return joins
}