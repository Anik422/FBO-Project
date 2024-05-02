const buy_now = document.getElementById("buy_now");
const membership_discerption = document.getElementById(
  "membership_discerption"
);
const membership_price = document.getElementById("membership_price");

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
  buy_now.href = `/memberships/${membershipPlanSlug}/${packageSlug}/`;
}
