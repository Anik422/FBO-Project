const buy_now = document.getElementById("buy_now");
const membership_discerption = document.getElementById(
  "membership_discerption"
);
const membership_price = document.getElementById("membership_price");

let packageSlugVal = '';
let membershipPlanSlugVal = ''

buy_now.addEventListener("click", (e) => {
  let selectDate = document.getElementById("booking_date").value;
  if (selectDate == "") {
    document.getElementById("dateError").innerHTML = "Please select a date.";
    document.getElementById("dateError").style.display = "inline";
    e.preventDefault();
  } else if (packageSlugVal == "") {
    alert("Please select a package.");
    e.preventDefault();
  } else {
    document.getElementById("membership_form").action = `/subscription/order/${membershipPlanSlugVal}/${packageSlugVal}/`;
  }
});

function changePrice(
  price,
  package,
  discerption,
  packageSlug,
  membershipPlanSlug
) {
  const btn = document.getElementById(packageSlug);
  const allBtn = document.querySelectorAll(".btns");
  allBtn.forEach((btn) => {
    btn.classList.remove("bg-gray-300");
  });
  btn.classList.add("bg-gray-300");
  membership_price.innerHTML = `$${price} / ${package}`;
  membership_discerption.innerHTML = discerption;
  // buy_now.href = `/subscription/${membershipPlanSlug}/${packageSlug}/`;
  packageSlugVal = packageSlug;
  membershipPlanSlugVal = membershipPlanSlug
}

const quantity = document.getElementById("quantity");
const increment = document.getElementById("increment");
const decrement = document.getElementById("decrement");

increment.addEventListener("click", () => {
  if (parseInt(quantity.value) >= 10) {
    increment.disabled = true;
  } else {
    quantity.value = parseInt(quantity.value) + 1;
    decrement.disabled = false;
  }
});

decrement.addEventListener("click", () => {
  if (parseInt(quantity.value) <= 1) {
    decrement.disabled = true;
  } else {
    quantity.value = parseInt(quantity.value) - 1;
    increment.disabled = false;
  }
});

function formatDate(date) {
  var d = new Date(date),
    month = "" + (d.getMonth() + 1),
    day = "" + d.getDate(),
    year = d.getFullYear();

  if (month.length < 2) month = "0" + month;
  if (day.length < 2) day = "0" + day;

  return [year, month, day].join("-");
}

function checkDate() {
  var selectedDate = formatDate(document.getElementById("booking_date").value);
  var today = formatDate(new Date());

  if (selectedDate < today) {
    decrement.getElementById("dateError").innerHTML =
      "Please select a date equal to or later than today.";
    document.getElementById("dateError").style.display = "inline";
  } else {
    document.getElementById("dateError").style.display = "none";
    document.getElementById("dateError").innerHTML = "";
  }
}
