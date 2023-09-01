# Notes

This is my structure to taking notes and journaling on the computer.

My goals are simple tooling that can be read by any other app on a different layer outside the scope of this document.

### Terms

These are inspired by [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)

- YYYY
4-digit year

- DDD
zero-padded 3-digit [ordinal day of the implied year](https://miniwebtool.com/day-of-year-calendar/)

### Searching

Most modern operating systems do full text search by default.

## A prime workspace

Create a folder/directory structure under the user's `$HOME` folder/directory:

```
workspace/
	journal/
		YYYY/
			DDD-title-of-entry.md
		2023/
			001-new-years-day.md
			002-we-take-advantage-of-how-filesystems-sort-numbers.md
			069-watched-svb-fail-also-nice.md
			100-today-i-explained-to-reddit-how-to-journal.md

	reference/
		# This repository

```

## In a project

These can be any project that will generate a lot of artifacts

```
corporate-app-acme/
	.local/
		YYYY/
			DDD-title-of-entry.md
		2023/
			001-new-years-day.md
			002-we-take-advantage-of-how-filesystems-sort-numbers.md
			069-watched-svb-fail-also-nice.md
			100-today-i-explained-to-reddit-how-to-journal.md
```
