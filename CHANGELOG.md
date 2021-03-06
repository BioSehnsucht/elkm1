# Changelog
All notable changes to this project will be documented in this file.
This project follows [Semantic Versioning](https://semver.org/).

## [0.4.1]
- Add serial io dependency

## [0.4.0]
- Breaking change: no longer need to call 
  elk.loop.run_until_complete(elk.connect()); now call elk.connect()
- Retrieve counter values that have a description
- Fix for HASS Recorder errors about not being JSON serializable

## [0.3.7]
- Add asyncio serial support
  - Add test program to test serial support (bin/test-serial); requires data
    file that can be grokked from debug output of bin/elk
- Add proper command line parsing for bin/elk including URL as param
  - URL can also be read from environment variable ELKM1_URL
- Add reconnect logic with exponetial backoff
- Add pause writing to Elk when in remote programming mode
- Add const for format of setting
- Add const for RP mode
- Change thermostat const to match semantics of other const (e.g.: FAN_ON
  changed to ON, MODE_AUTO to AUTO, etc). Makes for better formatting when
  using pretty_const

## [0.3.6]
- Start of cleanup of cmdr.py; using attrs lib
- Change return on pretty_const to string (was tuple)
- First cut of adding disconnect handling
  - Reconnect to be handler by client; will get a callback on disconnect
- Fix alarm armup/state/etc to char from int

## [0.3.5]
- Lint cleanup
- Constants now all uppercase with underscores (can use pretty_const to print)
- Added encode for az, decode for AZ (no handler yet)

## [0.3.4]
Fix syntax; more descriptive docstrings

## [0.3.3]
- Make elk attribute in Element private
- Allow separator in default_name() to be specified
- Add constants for arming, alarms

## [0.3.1]
- Add elk attribute to Element

## [0.3.0]
- Add NS, NZ to no plans to implement list
- Make default name 1-based
- Add helpers to Output
- Add helpers to Light
- Add helper to Counter
- Add helper to Task
- Add helpers to Area
- Add handler for task change (TC) message
- Add thermostat setting
- Add helper for Setting (custom value)
- Added const for thermostat setting
- Added pretty_const (see test_util.py for API)

## [0.2.1] - 2018-04-13
- Add display message encoder

## [0.2.0] - 2018-04-13
- Add thermostats (not Omnistat)

## [0.1.1] - 2018-04-08
### Added
- MANIFEST.in to include bin files and LICENSE in distro

### Changed
- Makefile updated to include build and upload rules

## [0.1.0] - 2018-04-07
### Added
- Initial version, see README.rst for overview of project.

### Changed

### Removed
