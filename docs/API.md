# Fabrication Tools API

## Overview

The Fabrication Tools project is organized into reusable modules to separate
Revit API interactions, business logic, geometry calculations, and user interface
code.

## Module Structure

### lib/collector.py

Responsible for collecting FabricationPart elements from the active Revit document.

Methods:

- get_all_parts()
- get_part_count()
- get_sample()

---

### lib/fabrication.py

Provides helper methods for reading fabrication-specific properties.

Examples:

- Service Name
- Specification
- CID
- Item Number
- Product Entry

---

### lib/geometry.py

Provides geometry calculations.

Examples:

- Centerline length
- Midpoint
- Direction vectors
- Distance calculations

---

### lib/hangers.py

Contains the hanger placement engine.

Responsibilities:

- Calculate support locations
- Apply spacing rules
- Avoid fittings
- Create fabrication hangers

---

### lib/config.py

Loads and saves user settings.

Examples:

- Default spacing
- End offset
- Trapeze threshold
- Clearance rules

---

## Future Modules

- Trapeze Engine
- Collision Detection
- Reporting
- WPF User Interface
- QA/QC Checker