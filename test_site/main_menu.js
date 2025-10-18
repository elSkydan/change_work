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
                        window.location.href = "dashboard.html";
                        break;
                    case "Profile":
                        window.location.href = "profile.html";
                        break;
                    case "VisitLog":
                        window.location.href = "Visitorlog.html";
                        break;
                    case "Exit":
                        window.location.href = "index.html";
                        break;
                    case "Comments":
                        window.location.href = "comments.html";
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


// comments.js
// Хранение в localStorage под ключом "mf_comments"
// обеспечивает: добавить, отрисовать, редактировать, удалять

(function () {
  const STORAGE_KEY = "mf_comments_v1";

  // utils
  function $(id){ return document.getElementById(id) }
  function escapeHtml(s){
    return s.replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'})[c]);
  }
  function nowFormatted(){ return new Date().toLocaleString() }

  // toast
  const toastEl = $("toast");
  function showToast(msg, ms = 2000){
    if(!toastEl) return;
    toastEl.textContent = msg;
    toastEl.classList.add("show");
    clearTimeout(toastEl._t);
    toastEl._t = setTimeout(()=> toastEl.classList.remove("show"), ms);
  }

  // read/write storage
  function loadComments(){
    try{
      return JSON.parse(localStorage.getItem(STORAGE_KEY) || "[]");
    }catch(e){ return [] }
  }
  function saveComments(arr){
    localStorage.setItem(STORAGE_KEY, JSON.stringify(arr));
  }

  // render list
  const commentsList = $("commentsList");
  function render(){
    if(!commentsList) return;
    commentsList.innerHTML = "";
    const items = loadComments().slice().reverse(); // последние сверху
    if(items.length === 0){
      const empty = document.createElement("div");
      empty.className = "empty";
      empty.textContent = "Пока нет комментариев — будь первым!";
      commentsList.appendChild(empty);
      return;
    }

    items.forEach(item => {
      const row = document.createElement("div");
      row.className = "comment";
      // initials
      const initials = (item.nickname || "U").trim().split(/\s+/).map(n=>n[0]).slice(0,2).join("").toUpperCase();
      // body
      row.innerHTML = `
        <div class="avatar" aria-hidden="true">${escapeHtml(initials)}</div>
        <div class="comment-body">
          <div class="meta">
            <div class="nickname">${escapeHtml(item.nickname)}</div>
            <div class="time">${escapeHtml(item.date)}</div>
          </div>
          <div class="text" data-id="${item.id}">${escapeHtml(item.text)}</div>
        </div>
        <div class="actions">
          <button class="action-btn edit" data-id="${item.id}">Ред.</button>
          <button class="action-btn delete" data-id="${item.id}">Удалить</button>
        </div>
      `;
      commentsList.appendChild(row);
    });

    // attach handlers
    commentsList.querySelectorAll(".action-btn.edit").forEach(btn=>{
      btn.addEventListener("click", ()=> startEdit(btn.dataset.id));
    });
    commentsList.querySelectorAll(".action-btn.delete").forEach(btn=>{
      btn.addEventListener("click", ()=> removeComment(btn.dataset.id));
    });
  }
    function getLastVisitor() {
    try {
      const visitors = JSON.parse(localStorage.getItem("visitors") || "[]");
      return visitors.length ? visitors[visitors.length - 1] : null;
    } catch (e) {
      return null;
    }
  }

  const currentUser = getLastVisitor();
  if (currentUser && $("nickname")) {
    $("nickname").value = currentUser.firstname + " " + currentUser.secondname;
    $("nickname").readOnly = true; // 🔒 фиксируем имя
    $("nickname").classList.add("readonly");
  }
  // form logic
  const form = $("commentForm");
  const nicknameInput = $("nickname");
  const textInput = $("commentText");
  const charCount = $("charCount");
  const clearFormBtn = $("clearForm");
  const clearAllBtn = $("clearAll");

  if(charCount && textInput){
    textInput.addEventListener("input", ()=> {
      charCount.textContent = `${textInput.value.length} / ${textInput.maxLength || 1000}`;
    });
  }

  // create
  function addComment(nickname, text){
    const arr = loadComments();
    const id = Date.now().toString(36) + "-" + Math.random().toString(36).slice(2,6);
    arr.push({ id, nickname, text, date: nowFormatted() });
    saveComments(arr);
    render();
    showToast("Комментарий сохранён");
  }

  // delete (silent, без confirm)
  function removeComment(id){
    let arr = loadComments();
    arr = arr.filter(it => it.id !== id);
    saveComments(arr);
    render();
    showToast("Комментарий удалён");
  }

  // edit in-place: копируем данные в форму, помечаем режим редактирования
  let editingId = null;
  function startEdit(id){
    const arr = loadComments();
    const item = arr.find(it => it.id === id);
    if(!item) return;
    nicknameInput.value = item.nickname;
    textInput.value = item.text;
    textInput.focus();
    editingId = id;
    showToast("Редактирование: внесите изменения и нажмите Отправить");
    // update charcount
    if(charCount) charCount.textContent = `${textInput.value.length} / ${textInput.maxLength || 1000}`;
  }
  function finishEdit(){
    if(!editingId) return;
    const arr = loadComments();
    const idx = arr.findIndex(it => it.id === editingId);
    if(idx === -1) return;
    arr[idx].nickname = nicknameInput.value.trim() || arr[idx].nickname;
    arr[idx].text = textInput.value.trim() || arr[idx].text;
    arr[idx].date = nowFormatted();
    saveComments(arr);
    editingId = null;
    render();
    showToast("Комментарий обновлён");
  }

  // clear all
  function clearAll(){
    saveComments([]);
    render();
    showToast("Все комментарии удалены");
  }

// bind form submit
if (form) {
  form.addEventListener("submit", function (e) {
    e.preventDefault();

    const nick = (nicknameInput.value || "").trim();
    const text = (textInput.value || "").trim();

    if (!text) {
      showToast("Комментарий не может быть пустым");
      return;
    }

    // если ник не указан — используем имя текущего пользователя или "Anonymous"
    const nicknameValue =
      nick || (currentUser ? `${currentUser.firstname} ${currentUser.secondname}` : "Anonymous");

    if (editingId) {
      finishEdit();
      form.reset();
    } else {
      addComment(nicknameValue, text);
      form.reset();
    }

    if (charCount) {
      charCount.textContent = `0 / ${textInput.maxLength || 1000}`;
    }
  });
}

// очистка формы
if (clearFormBtn) {
  clearFormBtn.addEventListener("click", () => {
    form.reset();
    if (charCount)
      charCount.textContent = `0 / ${textInput.maxLength || 1000}`;
  });
}

// очистка всех комментариев
if (clearAllBtn) {
  clearAllBtn.addEventListener("click", () => {
    clearAll();
  });
}

  // initial render
  render();
})();
