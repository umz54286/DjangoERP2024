$(document).ready(function () {
  if ($(window).width() > 768) {
    $("#collapseBuy").attr("class", "collapse show");
    $("#collapseSell").attr("class", "collapse show");
    $("#collapseStock").attr("class", "collapse show");
    $("#collapsePrint").attr("class", "collapse show");
  }
});
