
### Core Search Syntax

You will use a combination of three specific Google operators:

* `site:` (Limits results to a specific government domain)
* `filetype:` (Forces Google to show only files, like PDFs or Excel sheets, ignoring normal webpages)
* `intext:` (Looks for specific keywords inside those files)

### Federal Government

**1. The "Staff Directory" PDF Hunt**
Agencies often upload phone directories or organizational charts as PDFs.

* **Search Pattern:**
`site:[agency].gov filetype:pdf "directory" "email"`
* **Example (EPA):**
`site:epa.gov filetype:pdf "staff directory" "@epa.gov"`
* **What you'll find:** Internal phone lists, "Who to Call" guides, or org charts with direct lines.

**FOIA/PRR Officers**
Every agency has a [Freedom of Information Act (FOIA)](/osint/foia-prr.md) officer who must be reachable by the public. Their email often reveals the agency's standard email format.

* **Search Pattern:**
`site:[agency].gov "FOIA contact" "@[agency].gov"`
* **Why this helps:** If the FOIA officer is `john.smith@agency.gov`, you now know the format is `first.last`. You can then guess the email of the official you actually want to reach.

**3. The "Press Release" Contact**

* **Search Pattern:**
`site:[agency].gov "media contact" "immediate release" "@[agency].gov"`

### Washington State

Washington State has a specific digital footprint. The primary domain is `wa.gov`, but agencies have subdomains (e.g., `leg.wa.gov` for the legislature).

**Spreadsheets**
State governments love Excel. They use it for vendor lists, employee rosters, and conference registrations. These are often indexed by mistake.

* **Search Pattern (Spreadsheets):**
`site:wa.gov filetype:xlsx "email" "name" "title"`
* **Search Pattern (Legislative Staff):**
`site:leg.wa.gov filetype:pdf "staff list" "@leg.wa.gov"`

**2. Agency Specific Search**

* **Standard WA Format:** `firstname.lastname@agency.wa.gov`
* **Search Pattern:**
`site:wa.gov "program manager" "@*.wa.gov"`
*(The `*` is a wildcard that helps find different agency subdomains).*

### City Government (Seattle & General)

**1. The "Meeting Minutes" Artifact**
City Council meetings produce "minutes" (summaries) that often list the email addresses of attendees or presenters.

* **Search Pattern:**
`site:seattle.gov filetype:pdf "minutes" "@seattle.gov" -site:seattle.gov/contact`
* **Why the `-site:` part?** This excludes the generic "Contact Us" pages so you dig deeper into the files.

**Project Manager Artifacts**

* **Search Pattern:**
`site:seattle.gov "project manager" "questions" "@seattle.gov"`
* **Search Pattern (bids/contracts):**
`site:seattle.gov filetype:pdf "RFP" "contact" "@seattle.gov"`

**3. Seattle Specific Email Format**

* **Standard:** `firstname.lastname@seattle.gov`
* **Council Members:** Usually `firstname.lastname@seattle.gov` directly, though they publicly advertise `council@seattle.gov`.


### **Summary of "Artifact" Keywords**

Swap out these keywords to find different types of documents:

| Artifact Type | Keywords to use with `filetype:pdf` or `filetype:xlsx` |
| --- | --- |
| **Direct Contact Info** | "POC", "Point of Contact", "Staff List", "Roster", "Directory" |
| **External Leaks** | "Attendee List", "Sign-in Sheet", "Conference", "Agenda" |
| **Spending/Money** | "Budget", "Procurement", "RFP", "Vendor" |
