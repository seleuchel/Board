function formatDate(dateString) {
    let date = new Date(dateString);
    if (isNaN(date.getTime())) return "";
    return date.toISOString().split("T")[0]; // YYYY-MM-DD 형식 변환
}



$(document).ready(function () {

    // add new row
    $("#addRowBtn").click(function () {
        let newRow = `
            <tr data-id="">
                <td><input type="checkbox" data-field="vul_ok"></td>
                <td contenteditable="true" data-field="srv_name"></td>
                <td contenteditable="true" data-field="req_date"></td>
                <td contenteditable="true" data-field="sendmail_date"></td>
                <td contenteditable="true" data-field="adm_buseo"></td>
                <td contenteditable="true" data-field="adm_name"></td>
                <td contenteditable="true" data-field="srv_loc"></td>
                <td contenteditable="true" data-field="bigo"></td>
            </tr>
        `;
        $("#dataTable").append(newRow);
    });




    $("tbody").on("change", 'input[type="checkbox"][data-field="vul_ok"]', function () {
        let isChecked = $(this).prop("checked");
        $(this).attr("data-value", isChecked ? "true" : "false");
    });

    $("#saveBtn").click(function () {
        let posts = [];

        $("tbody tr").each(function () {
            let postData = {
                id: $(this).data("id"),
                vul_ok: $(this).find('[data-field="vul_ok"]').prop("checked"), // 체크박스 상태 반영
                srv_name: $(this).find('[data-field="srv_name"]').text().trim(),
                req_date: formatDate($(this).find('[data-field="req_date"]').text().trim()),
                sendmail_date: formatDate($(this).find('[data-field="sendmail_date"]').text().trim()),
                adm_buseo: $(this).find('[data-field="adm_buseo"]').text().trim(),
                adm_name: $(this).find('[data-field="adm_name"]').text().trim(),
                srv_loc: $(this).find('[data-field="srv_loc"]').text().trim(),
                bigo: $(this).find('[data-field="bigo"]').text().trim(),
            };

            let id = $(this).attr("id");
            if (id) {postData["id"] = id;}

            posts.push(postData);
        });

        $.ajax({
            url: "/post/update/",
            type: "POST",
            data: JSON.stringify({ posts: posts }),
            contentType: "application/json",
            headers: { "X-CSRFToken": getCSRFToken() },
            success: function (response) {
                alert("저장되었습니다!");
            },
            error: function (xhr, status, error) {
                console.log(xhr.responseText);
                alert("저장 중 오류가 발생했습니다.");
            
            },
        });
    });

    function getCSRFToken() {
        let csrfToken = null;
        document.cookie.split(";").forEach(function (cookie) {
            let parts = cookie.trim().split("=");
            if (parts[0] === "csrftoken") {
                csrfToken = parts[1];
            }
        });
        return csrfToken;
    }
});