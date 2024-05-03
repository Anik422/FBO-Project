const buy_now = document.getElementById("buy_now");
const membership_discerption = document.getElementById(
  "membership_discerption"
);
const membership_price = document.getElementById("membership_price");

buy_now.addEventListener("click", (e) => {
  console.log(buy_now.href, "@@@@@@@@@@@");
  if (buy_now.href === "javascript:void(0)") {
    e.preventDefault();
    alert("Please select a package to continue");
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
  buy_now.href = `/subscription/${membershipPlanSlug}/${packageSlug}/`;
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
