document.addEventListener("DOMContentLoaded", function () {
    // ====== МЕНЮ НАВИГАЦИИ ======
    const menu = document.getElementById("MainMenu");
    if (menu) {
        menu.addEventListener("click", function (event) {
            if (event.target.tagName === "A") {
                event.preventDefault();
                const targetId = event.target.id;

                switch (targetId) {
                    case "Home":
                        window.location.href = "index.html";
                        break;
                    case "Profile":
                        window.location.href = "profile.html";
                        break;
                    case "VisitLog":
                        window.location.href = "Visitorlog.html";
                        break;
                    default:
                        console.warn("Неизвестный пункт меню:", targetId);
                }
            }
        });
    }

    // ====== ЛОГИКА ФОРМЫ (index.html) ======
    const visitorForm = document.getElementById("VisitorForm");
    const resetBtn = document.getElementById("resetBtn");

    if (visitorForm) {
    visitorForm.addEventListener("submit", function (e) {
        e.preventDefault();

        const firstname = document.getElementById("firstname").value.trim();
        const secondname = document.getElementById("secondname").value.trim();

        if (!firstname || !secondname) {
            // Если поля пустые — просто не выполняем, без alert
            return;
        }

        let visitors = JSON.parse(localStorage.getItem("visitors") || "[]");
        visitors.push({ firstname, secondname, date: new Date().toLocaleString() });
        localStorage.setItem("visitors", JSON.stringify(visitors));

        visitorForm.reset();

        // Переход на дашборд
        window.location.href = "dashboard.html";
    });
}

    if (resetBtn) {
        resetBtn.addEventListener("click", function () {
            document.getElementById("firstname").value = "";
            document.getElementById("secondname").value = "";
        });
    }

    // ====== ТАБЛИЦА НА VisitLog.html ======
    const visitorsTable = document.getElementById("visitorsTable");
if (visitorsTable) {
    const tbody = visitorsTable.querySelector("tbody");

    function renderVisitors() {
        tbody.innerHTML = ""; // очищаем таблицу перед отрисовкой
        const visitors = JSON.parse(localStorage.getItem("visitors") || "[]");

        if (visitors.length === 0) {
            const emptyRow = document.createElement("tr");
            emptyRow.innerHTML = `<td colspan="3" style="text-align:center; color:#777;">No visitors yet</td>`;
            tbody.appendChild(emptyRow);
        } else {
            visitors.forEach((v, index) => {
                const row = document.createElement("tr");
                row.innerHTML = `
                    <td>${v.firstname}</td>
                    <td>${v.secondname}</td>
                    <td>
                        <button class="delete-btn" data-index="${index}">❌ Delete</button>
                    </td>
                `;
                tbody.appendChild(row);
            });

            // Навешиваем обработчик на кнопки удаления
            const deleteButtons = tbody.querySelectorAll(".delete-btn");
            deleteButtons.forEach(btn => {
                btn.addEventListener("click", function () {
                    const i = parseInt(this.dataset.index);
                    let visitors = JSON.parse(localStorage.getItem("visitors") || "[]");
                    visitors.splice(i, 1); // удаляем запись по индексу
                    localStorage.setItem("visitors", JSON.stringify(visitors));
                    renderVisitors(); // перерисовываем таблицу
                });
            });
        }
    }

    renderVisitors();
}

    // ====== КНОПКА ОЧИСТКИ ЛОГА ======
    const clearLogBtn = document.getElementById("clearLogBtn");
    if (clearLogBtn) {
        clearLogBtn.addEventListener("click", function () {
            if (confirm("Are you sure you want to clear all visitors?")) {
                localStorage.removeItem("visitors");
                alert("Visitor log cleared!");
                location.reload();
            }
        });
    }
});
