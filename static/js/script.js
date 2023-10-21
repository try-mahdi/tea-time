document.addEventListener("DOMContentLoaded", function () {
    const rows = document.querySelectorAll("tbody tr");
    const deleteButtons = document.querySelectorAll(".delete-button");

    rows.forEach((row, index) => {
        row.addEventListener("click", () => {
            // Hide all delete buttons
            deleteButtons.forEach(button => button.style.display = "none");

            // Show the delete button for the clicked row
            const deleteButton = row.querySelector(".delete-button");
            deleteButton.style.display = "block";
        });

        // Prevent the button click from triggering the row click
        const deleteButton = row.querySelector(".delete-button");
        deleteButton.addEventListener("click", (event) => {
            event.stopPropagation();
            // Implement your delete logic here
            // You can access the data for the row using the 'index'
            // For example, orders[index] represents the data for the clicked row
            console.log("Delete clicked for row", index);
        });
    });
});
