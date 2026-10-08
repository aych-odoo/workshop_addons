# Build a Real Estate App with Odoo 20

This repository is a teaching companion to Odoo's [Server framework 101 tutorial](https://www.odoo.com/documentation/20.0/developer/tutorials/server_framework_101.html). The [tutorial source](https://github.com/odoo/documentation/tree/20.0/content/developer/tutorials/server_framework_101) gives the framework explanation and exercises; this guide connects those ideas to the code checkpoints here.

The `master` branch contains this complete guide and no addon code. The `solution` branch adds the application one chapter at a time; Chapter 15 is a review checkpoint with no new addon code. Add this repository to Odoo's addons path when working through the exercises.

Start your own learning branch from `master`. For each chapter, read the objectives and **Build this chapter**, implement the changes, then compare your result with the matching commit on `solution` using `git show`. **What we built** summarizes that chapter's solution checkpoint. The exploration task helps connect the exercise to the wider Odoo framework.

## Chapter 1: Architecture overview

[Official chapter](https://www.odoo.com/documentation/20.0/developer/tutorials/server_framework_101/01_architecture.html)

**Objectives**

- Identify Odoo's presentation, business logic, and data tiers.
- Explain how an addon groups models, views, and data files into an installable feature.

**Build this chapter**

- Copy the Odoo Community `.gitignore` into this repository. Do not create addon files yet. Locate an installed addon's manifest, a model, a view, and a data file in the Odoo source tree.
- Draw how a request moves between browser, Python model, and PostgreSQL. Identify where each file fits.

**What we built:** The first commit contains this complete course guide and a copy of the Odoo Community `.gitignore`. There is no addon code yet.

**Concepts worth learning:** Python implements server logic, PostgreSQL stores records, and the web client presents them. An addon belongs on the addons path and is installed for a particular database; putting files on disk alone does not install it.

**Explore further:** Pick an installed Odoo addon. Find its manifest, a model, and a view. Trace one field from its Python declaration to what a user sees in the browser.

## Chapter 2: A new application

[Official chapter](https://www.odoo.com/documentation/20.0/developer/tutorials/server_framework_101/02_newapp.html)

**Objectives**

- Create the smallest discoverable Odoo addon.
- Distinguish a dependency from the flag that displays a module as an app.

**Build this chapter**

- Create `estate/` with an empty `__init__.py` and a `__manifest__.py` containing the name `Real Estate`, author `Ayush Chauhan`, license `LGPL-3`, description `Manage real estate listings, types, tags, offers, and their sales workflow`, `depends: ['base']`, and `application: True`.
- Copy the supplied image to `estate/static/description/icon.png` without resizing it.
- Keep the addon empty for now: no model, security file, menu, or view is introduced in this checkpoint.

**What we built:** `estate/__init__.py` makes the directory a Python package. `estate/__manifest__.py` declares the app name, author, license, description, `base` dependency, and `application=True`. The addon has an icon and can be installed, but has no business model or menu yet.

**Concepts worth learning:** The manifest declares module metadata and dependencies. The addons path tells Odoo where to find modules; the database records which modules are installed.

**Explore further:** Update the Apps list and find Real Estate. Why does an installable app have no main menu at this checkpoint?

## Chapter 3: Models and basic fields

[Official chapter](https://www.odoo.com/documentation/20.0/developer/tutorials/server_framework_101/03_basicmodel.html)

**Objectives**

- Define a model and choose field types for property data.
- Relate a Python model to its database table and automatic fields.

**Build this chapter**

- Create `estate/models/estate_property.py` with an `estate.property` model and import it through both `estate/models/__init__.py` and `estate/__init__.py`.
- Add `name` (`Char`, required), `description` (`Text`), `postcode` (`Char`), and `date_availability` (`Date`).
- Add `expected_price` (`Float`, required), `selling_price` (`Float`), `bedrooms`, `living_area`, `facades`, and `garden_area` (`Integer`), plus `garage` and `garden` (`Boolean`).
- Add `garden_orientation` as a `Selection` with north, south, east, and west keys. Defaults, lifecycle state, and custom views arrive in later chapters.

**What we built:** `estate.property` stores the name, description, postcode, availability, prices, rooms, living area, and garden details. Name and expected price are required; garden orientation uses stored selection keys and readable labels.

**Concepts worth learning:** The ORM maps `estate.property` to the `estate_property` table and handles ordinary record operations. Odoo supplies fields such as `id` and `create_date` without declarations in the model.

**Explore further:** Compare the model's fields with the table columns. Which values belong in a selection field, and which might deserve a related model?

## Chapter 4: Security: a brief introduction

[Official chapter](https://www.odoo.com/documentation/20.0/developer/tutorials/server_framework_101/04_securityintro.html)

**Objectives**

- Grant model access to a specific user group.
- Explain why a menu or view cannot replace access rights.

**Build this chapter**

- Create `estate/security/ir.access.csv` with the Odoo 20 columns `id,name,model_id,group_id/id,operation,domain`.
- Add one row for `estate.property`, granting `crud` to `base.group_user`, and list the CSV under `data` in the manifest.

**What we built:** `estate/security/ir.access.csv` grants internal users create, read, update, and delete access to properties, and the manifest loads the CSV file. This Odoo 20 checkout uses an `operation` column in `ir.access.csv`; the tutorial may show the older `ir.model.access.csv` layout.

**Concepts worth learning:** Access rights apply to model operations regardless of which screen calls them. Data files load on installation or upgrade, so editing a CSV alone does not update an installed database.

**Explore further:** Compare an internal user's access with a user outside `base.group_user`. Find a standard addon with both access rights and record rules. What extra question do record rules answer?

## Chapter 5: Finally, some UI to play with

[Official chapter](https://www.odoo.com/documentation/20.0/developer/tutorials/server_framework_101/05_firstui.html)

**Objectives**

- Connect a menu to a model through a window action.
- Use defaults, lifecycle fields, and copy behavior deliberately.

**Build this chapter**

- Add `active=True` and a required `state` selection: `new`, `offer_received`, `offer_accepted`, `sold`, `cancelled`. Default to `new` and set `copy=False`.
- Default `bedrooms` to 2 and `date_availability` to today plus three months. Do not copy availability or selling price; make selling price read-only.
- Define a `Properties` window action for `estate.property` with `list,form` view modes. Add menus Real Estate > Advertisements > Properties and load the action and menu XML in the manifest. Let Odoo generate the actual views for now.

**What we built:** Real Estate > Advertisements > Properties opens `estate.property` through Odoo's generated views. Properties start with two bedrooms, an availability date three months ahead, `active=True`, and state New. Availability and selling price are not copied when a property is duplicated.

**Concepts worth learning:** A menu provides navigation, an action chooses what to open, and a view controls presentation. Reserved fields such as `active` affect framework behavior; `copy=False` affects duplication rather than creation.

**Explore further:** Create and duplicate a property, then archive one. Which values were copied, recalculated, or hidden from the normal list, and why?

## Chapter 6: Basic views

[Official chapter](https://www.odoo.com/documentation/20.0/developer/tutorials/server_framework_101/06_basicviews.html)

**Objectives**

- Design list, form, and search views for different user tasks.
- Explain the difference between filtering records and grouping results.

**Build this chapter**

- Define a property list with `name`, `postcode`, `bedrooms`, `living_area`, `expected_price`, `selling_price`, and `date_availability` columns.
- Define a form with the property name as its title; put postcode and availability in one group, prices in another, and description, rooms, area, facades, garage, and garden fields on a Description tab.
- Define search fields for name, postcode, living area, and bedrooms. Add an Available filter for states New or Offer Received and a Postcode group-by filter directly inside `<search>`, without a wrapping `<group>`.
- Leave `string` off the root `<list>`, `<form>`, and `<search>` tags; keep labels where they identify fields, filters, or pages.

**What we built:** A property list shows summary columns, a form organizes fields for editing, and a search view supports finding available properties and grouping by postcode. These views replace generated presentation without redefining the model.

**Concepts worth learning:** A search domain selects records. A grouping context changes how selected records appear. XML views describe the interface; the Python model remains the source of field definitions.

**Explore further:** Search for a property, apply Available, and group by postcode. Find a model field absent from one view. Does its database column still exist?

## Chapter 7: Relations between models

[Official chapter](https://www.odoo.com/documentation/20.0/developer/tutorials/server_framework_101/07_relations.html)

**Objectives**

- Choose between `Many2one`, `Many2many`, and `One2many` relationships.
- Reuse existing partner and user models instead of duplicating their data.

**Build this chapter**

- Create `estate.property.type` and `estate.property.tag` with required `name` fields. Create `estate.property.offer` with `price`, accepted/refused `status`, required `partner_id` (`res.partner`), and required `property_id` (`estate.property`, cascade on delete).
- On the property model, add `property_type_id` (`Many2one`), `tag_ids` (`Many2many`), `offer_ids` (`One2many` through `property_id`), `partner_id` (Buyer, `res.partner`, not copied), and `user_id` (Salesperson, `res.users`, default current user).
- Grant internal users `crud` access to the three new models. Add Configuration > Property Types and Property Tags menus with window actions; let Odoo generate their list and form views at this checkpoint. Give offers explicit list and form views but no standalone menu.
- Show type and tags in the property list and form, type in search, offers on an Offers tab, and buyer and salesperson on an Other Info tab.

**What we built:** Properties connect to types, tags, buyers, salespeople, and offers. Types and tags have configuration actions, generated views, and access rights; offers are entered from a property's Offers tab. Each offer points back to its property through a required `property_id`.

**Concepts worth learning:** A `Many2one` links to one record, a `Many2many` connects sets of records, and a `One2many` shows records linked through an inverse `Many2one`. Relations shape both storage and the form workflow.

**Explore further:** Create one property with several offers and tags. Which field stores the offer's property link? Why does the property not need a column for every offer?

## Chapter 8: Computed fields and onchanges

[Official chapter](https://www.odoo.com/documentation/20.0/developer/tutorials/server_framework_101/08_compute_onchange.html)

**Objectives**

- Derive values from other fields and declare dependencies.
- Distinguish a computed field with an inverse from a form onchange.

**Build this chapter**

- Add computed `total_area` (`living_area + garden_area`) and `best_price` (highest offer price) to properties, with dependencies on their source fields. Display total area on the Description tab and best price with the prices.
- Add offer `validity` (`Integer`, default 7) and `date_deadline` (`Date`). Compute the deadline from creation date, or today for a new offer, plus `relativedelta(days=validity)`; add an inverse that uses the total days between dates when the deadline is edited.
- Show validity and deadline in both offer views. Add a garden onchange that sets area to 10 and orientation to North when selected, and clears both when deselected.

**What we built:** `total_area` adds living and garden areas, and `best_price` selects the highest offer. Offers have a validity period and computed deadline with an inverse method. A garden onchange suggests an area and orientation when Garden is selected and clears them when it is deselected.

**Concepts worth learning:** `@api.depends` tells Odoo when to recompute. An inverse lets a user edit a computed result by updating its inputs. An onchange assists interactive form entry; model logic still matters for imports and other non-form writes.

**Explore further:** Change an offer deadline and inspect its validity. For an offer created through code, which values still compute and which form suggestion would not run?

## Chapter 9: Ready for some action?

[Official chapter](https://www.odoo.com/documentation/20.0/developer/tutorials/server_framework_101/09_actions.html)

**Objectives**

- Connect buttons to public model methods.
- Keep property and offer state transitions consistent.

**Build this chapter**

- Add property `action_sold` and `action_cancel` methods. Reject selling a cancelled property or cancelling a sold one; otherwise set its state.
- Add offer `action_accept` and `action_refuse`. Accepting assigns `partner_id`, `selling_price`, and `state` directly on the property; reject a second accepted offer and acceptance for sold or cancelled properties. Refusing sets Refused, but must not undo an accepted offer. The four action methods need no `return True`.
- Put Sold and Cancel buttons in the property form header. Put Accept and Refuse buttons only in the offer list, using `type="object"` and `check`/`cancel` icons; keep the offer form free of action buttons.

**What we built:** Property buttons mark records Sold or Cancelled; offer buttons accept or refuse an offer. Accepting an offer sets the property's buyer, selling price, and Offer Accepted state. Server checks reject incompatible transitions and a second accepted offer.

**Concepts worth learning:** A `type="object"` button invokes a model method, but that method can also be called outside the form. Workflow rules belong in server logic, not only in button visibility.

**Explore further:** Draw the allowed property states and transitions. What should happen if two offers are accepted in sequence, or someone tries to cancel a sold property through an API call?

## Chapter 10: Constraints

[Official chapter](https://www.odoo.com/documentation/20.0/developer/tutorials/server_framework_101/10_constraints.html)

**Objectives**

- Enforce data rules regardless of how records are created.
- Choose between database and Python constraints.

**Build this chapter**

- Add `models.Constraint` checks: expected price and offer price must be greater than zero; selling price must be at least zero; property type and tag names must each be unique.
- Add a Python constraint on expected and selling price: when a selling price is nonzero, require it to be at least 90% of expected price. Use Odoo's float comparison helpers for that ratio.

**What we built:** `models.Constraint` enforces positive expected and offer prices, nonnegative selling prices, and unique type and tag names. A Python constraint requires a nonzero selling price to be at least 90% of the expected price.

**Concepts worth learning:** Database constraints suit simple rules that must hold at storage time. Python constraints can express rules involving multiple fields and Odoo's comparison helpers. Neither depends on a particular form view.

**Explore further:** Predict which rule rejects a zero offer, a negative selling price, a duplicate type name, and an underpriced sale. Which kind of rule would be difficult to express as a simple database constraint?

## Chapter 11: Add the sprinkles

[Official chapter](https://www.odoo.com/documentation/20.0/developer/tutorials/server_framework_101/11_sprinkles.html)

**Objectives**

- Make an existing workflow easier to scan and navigate.
- Separate interface guidance from server-enforced rules.

**Build this chapter**

- Sort properties newest first, offers highest price first, and tags by name. Add tag `color`; add type `sequence`, related properties and offers, and a computed offer count. Give each offer a stored related `property_type_id` for filtering. Sort types by sequence then name.
- Introduce custom list and form views for property types and tags in this chapter. Make type order draggable in its list, add a Properties tab and Offers stat button to its form, and open the count in an offers action filtered by property type. Make tag and offer lists editable at the bottom; show a color picker for tags.
- Add a property status bar, colored tag widgets, row decorations, conditional button and garden-field visibility, and read-only offers after acceptance or closure. Hide the availability column by default while keeping it optional.
- Select Available by default in the property action and make living-area search mean a minimum area (`>=`). Decorate accepted and refused offers and hide their list action buttons once a status is set; do not add buttons to the offer form.

**What we built:** Status bars, colored tags, row decorations, inline editing, ordering, and a default Available filter improve the property screens. Property types can be reordered and show their properties plus an Offers count that opens matching offers.

**Concepts worth learning:** Widgets, decorations, visibility conditions, and stat buttons help users understand records. Search and ordering defaults affect presentation. These interface choices do not grant access or replace model constraints.

**Explore further:** Reorder types and open a type's Offers count. Find an action hidden by a view condition. What server rule protects the workflow when the UI is bypassed?

## Chapter 12: Inheritance

[Official chapter](https://www.odoo.com/documentation/20.0/developer/tutorials/server_framework_101/12_inheritance.html)

**Objectives**

- Extend record behavior and an existing Odoo model without replacing them.
- Apply business rules to offer creation and property deletion.

**Build this chapter**

- Add an `@api.ondelete(at_uninstall=False)` rule that permits deleting only New or Cancelled properties.
- Override offer `create` for batches: reject offers on accepted, sold, or cancelled properties; reject a price below the current highest offer; move properties with new offers to Offer Received.
- Extend `res.users` with assigned `property_ids`, limited to New or Offer Received properties. Import each model with its own `from . import module_name` line. Inherit the user form and add a read-only Properties tab after Preferences; load that view in the manifest.

**What we built:** Offer creation rejects a lower price than the current best offer and moves the property to Offer Received. An `@api.ondelete` method prevents deletion after a property enters an active or completed workflow. `res.users` gains assigned properties, and an inherited user form displays them in a Properties tab.

**Concepts worth learning:** Python inheritance can add behavior around standard CRUD operations. Model inheritance adds fields to an existing model; view inheritance places UI elements within an existing form. The original user model and view remain in their owning addon.

**Explore further:** Trace an offer's `create` call and a property's deletion rule. Why use the existing `res.users` record instead of introducing a separate salesperson model?

## Chapter 13: Interact with other modules

[Official chapter](https://www.odoo.com/documentation/20.0/developer/tutorials/server_framework_101/13_other_module.html)

**Objectives**

- Add optional accounting integration without making the core estate app depend on Accounting.
- Extend an action while preserving its original behavior.

**Build this chapter**

- Create a separate `estate_account` addon with package imports and a manifest declaring author `Ayush Chauhan`, license `LGPL-3`, description `Create a draft customer invoice when a real estate property is sold`, and dependencies on `estate` and `account`; leave `estate` independent of Accounting.
- Inherit `estate.property.action_sold`. Require a buyer on the property, call `super()` without storing or returning its result, then create a draft customer invoice (`account.move`, `move_type='out_invoice'`) for that buyer.
- Create two invoice lines with `Command.create`: real estate commission at 6% of selling price and administrative fees at 100, each with quantity 1. No new menu or view is needed.

**What we built:** The separate `estate_account` addon depends on `estate` and `account`. It extends the Sold action through `super()` and creates a draft customer invoice with commission of 6% of the selling price and an administrative fee of 100.

**Concepts worth learning:** Dependency direction determines which features can be installed independently. `Command.create` adds invoice lines while the invoice is created. Calling `super()` retains the estate workflow before the integration adds its effect.

**Explore further:** Draw the dependency graph for `base`, `estate`, `account`, and `estate_account`. What would change for users without Accounting if invoice creation lived inside `estate`?

## Chapter 14: A brief history of QWeb

[Official chapter](https://www.odoo.com/documentation/20.0/developer/tutorials/server_framework_101/14_qwebintro.html)

**Objectives**

- Render records as kanban cards with a QWeb template.
- Reason about the fields and grouping needed by a card view.

**Build this chapter**

- Add a property kanban view and include `kanban` between `list` and `form` in the Properties action.
- Group cards by `property_type_id` by default and disable dragging. In the QWeb `card` template, show name, expected price, and colored tags.
- Load `state` for conditions: show best offer only for Offer Received, and selling price for Offer Accepted or Sold.

**What we built:** Property cards show the name, expected price, tags, and the relevant offer or selling price for their state. Cards group by property type by default. Drag and drop is disabled so moving a card cannot silently change its type.

**Concepts worth learning:** The card template controls presentation for each record. Conditional rendering depends on fields loaded by the view, even when a field is not shown as its own line. List and kanban are views of the same records.

**Explore further:** Compare cards in New, Offer Received, Offer Accepted, and Sold states. Which condition determines the displayed price? What happens to grouping when a property's type changes?

## Chapter 15: The final word

[Official chapter](https://www.odoo.com/documentation/20.0/developer/tutorials/server_framework_101/15_final_word.html)

**Objectives**

- Explain the path from a property record to a draft invoice.
- Place each responsibility in the model, access data, view, action, constraint, or integration addon.

**Build this chapter**

- Add no addon code. Review each checkpoint and trace a property from creation through offers, acceptance, Sold, and the optional draft invoice.
- Map the implementation to its model, access CSV, views, actions, constraints, and integration dependency.

**What we built:** This is a review checkpoint with no new addon code. The earlier commits form an estate workflow, with optional invoicing supplied by `estate_account`.

**Concepts worth learning:** Models hold data and business rules, access data controls permissions, views present records, actions connect user intent to server methods, and dependencies compose features. Following one feature across these layers helps explain unfamiliar addons.

**Explore further:** Walk from creating a property to accepting an offer, marking it Sold, and finding its draft invoice. Inspect another Odoo addon and map one user action across the same layers. What can you explain from code, and what would you need to observe in a running database?
