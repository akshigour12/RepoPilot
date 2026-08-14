// ============================================
// Search Repositories
// ============================================

const searchInput = document.getElementById("searchInput");

if (searchInput) {

    searchInput.addEventListener("keyup", function () {

        const filter = this.value.toLowerCase();

        const rows = document.querySelectorAll("#repoTable tbody tr");

        rows.forEach(function (row) {

            const repoName = row.cells[1].textContent.toLowerCase();

            const language = row.cells[3].textContent.toLowerCase();

            if (
                repoName.includes(filter) ||
                language.includes(filter)
            ) {

                row.style.display = "";

            } else {

                row.style.display = "none";

            }

        });

    });

}


// ============================================
// Select All
// ============================================

const selectAll = document.getElementById("selectAll");

if (selectAll) {

    selectAll.addEventListener("change", function () {

        document.querySelectorAll(".repo-checkbox")
            .forEach(function (checkbox) {

                checkbox.checked = selectAll.checked;

            });

    });

}


// ============================================
// Auto Update Select All
// ============================================

const checkboxes = document.querySelectorAll(".repo-checkbox");

checkboxes.forEach(function (checkbox) {

    checkbox.addEventListener("change", function () {

        const checked =
            document.querySelectorAll(".repo-checkbox:checked").length;

        selectAll.checked = checked === checkboxes.length;

    });

});


// ============================================
// Confirm Delete
// ============================================

const form = document.querySelector("form");

if (form) {

    form.addEventListener("submit", function (event) {

        const action = document.getElementById("actionSelect").value;

        if (action === "delete") {

            const confirmDelete = confirm(
                "Delete selected repositories?\n\nThis action cannot be undone."
            );

            if (!confirmDelete) {

                event.preventDefault();

            }

        }

    });

}


// ============================================
// Dynamic Action Inputs
// ============================================

const actionSelect = document.getElementById("actionSelect");

if (actionSelect) {

    actionSelect.addEventListener("change", function () {

        const renamePrefixDiv =
            document.getElementById("renamePrefixDiv");

        const renameSuffixDiv =
            document.getElementById("renameSuffixDiv");

        const topicsDiv =
            document.getElementById("topicsDiv");

        const deleteWarning =
            document.getElementById("deleteWarning");

        renamePrefixDiv.classList.add("d-none");
        renameSuffixDiv.classList.add("d-none");
        topicsDiv.classList.add("d-none");
        deleteWarning.classList.add("d-none");

        switch (this.value) {

            case "rename":

                renamePrefixDiv.classList.remove("d-none");
                renameSuffixDiv.classList.remove("d-none");

                break;

            case "topics":

                topicsDiv.classList.remove("d-none");

                break;

            case "delete":

                deleteWarning.classList.remove("d-none");

                break;

        }

    });

}
