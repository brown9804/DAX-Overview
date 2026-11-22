function linkOrganizationLogo() {
  document.querySelectorAll("a.md-logo").forEach((link) => {
    link.href = "https://github.com/Cloud2BR-MSFTLearningHub";
    link.setAttribute("aria-label", "Cloud2BR OSS - Learning Hub on GitHub");
    const image = link.querySelector("img");
    if (image) image.alt = "Cloud2BR OSS - Learning Hub";
  });
}

document.addEventListener("DOMContentLoaded", linkOrganizationLogo);
if (typeof document$ !== "undefined") {
  document$.subscribe(linkOrganizationLogo);
}
