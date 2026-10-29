# Shopify section snippets

Copy only the needed `.liquid` file into a backed-up staging theme's `sections/` directory. Add the section in the theme editor and enter merchant-approved text. Test product variants, mobile layout, keyboard focus, cart behavior and FAQ text/schema match. Do not publish a theme or modify live production without written go-ahead in the job file.

`hero.liquid` supplies an image/copy CTA; `faq.liquid` emits matching FAQ schema; `sticky-atc.liquid` posts a selected variant through Shopify's product form; `trust-badges.liquid` displays only statements entered by the merchant. No unsupported trust claim is prefilled.
