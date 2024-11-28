$(document).ready(function () {
  if ($(window).width() > 768) {
    $("#collapseBuy").attr("class", "collapse show");
    $("#collapseSell").attr("class", "collapse show");
    $("#collapseStock").attr("class", "collapse show");
  }

  $("#myInput").on("keyup", function () {
    var value = $(this).val().toLowerCase();
    $("#inventoryDataTable tbody tr").filter(function () {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
    });
    $("#inventoryReportDataTable tbody tr").filter(function () {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
    });
    $("#dataTable tbody tr").filter(function () {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
    });
  });
  $("#sheetjsexport").click(function () {
    const table = document.getElementById("inventoryReportDataTable");
    const new_sheet = XLSX.utils.table_to_book(table);
    XLSX.writeFile(new_sheet, "庫存異動明細報表.xlsx");
  });
});
