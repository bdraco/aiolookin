# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [2.22.0]
### Added
- Optional parameter `campaign_id` to `/events/app/install` method

## [2.21.0]
### Added
- `viewers` to `BroadcastStatus`

## [2.20.0]
### Added
- Internal method for getting broadcasts
### Changed
- Move GRPC things to `platforms`

## [2.19.0]
### Changed
- Count bytes instead of characters for YouTube input length

## [2.18.0]
### Changed
- Allow zero length description

## [2.17.3]
### Fixed
- Graceful shutdown of `draw_promo`

## [2.17.2]
### Fixed
- Send statistics on exit

## [2.17.1]
### Added
- Logs for `item_presented_event`

## [2.17.0]
### Added
- Integration with 1Link

## [2.16.1]
### Removed
- Tarantool infrastructure dependencies

## [2.16.0]
### Changed
- Change minimum value for `drop_chance` to 0.001

## [2.15.0]
### Changed
- Change type for `drop_chance` to (float, int)
### Added
- Import for `received` promocodes
- Correct handling of `5xx` errors
- Internal method for getting present info

## [2.14.0]
### Changed
- Change type for `drop_chance` to float
### Added
- Add logs for draw presents

## [2.13.0]
### Added
- New HTTP error with code `platform_internal_error` when platforms return 500
### Fixed
- Crash when user participate in several campaigns

## [2.12.1]
### Fixed
- Handle `None` metadata for participant

## [2.12.0]
### Changed
- Use `platforms` version 3.3.1
- Add `is_participant` parameter to list of promo campaigns
- Add `game_id` query parameter to method for getting promo campaigns

## [2.11.0]
### Changed
- Only live streams are selected for drawing

## [2.10.1]
### Fixed
- `scheduled_start_time` is checked correctly according to ISO8601

## [2.10.0]
### Added
- Promo campaigns
- Method for getting status of a broadcast
- New parameter `platforms` in `stream_event`
### Fixed
- `date` value in statistics

## [2.9.1]
### Fixed
- Handle missing `streamName` parameter from Youtube's response
### Changed
- Allow duplicate `external_id` for broadcasts

## [2.9.0]
### Changed
- Add property `install_time` to `/events/app/install`

## [2.8.0]
### Added
- New statistic event `/events/app/install`
### Changed
- Add property `with_watermark` to `/events/stream/start`

## [2.7.0]
### Changed
- Migrated to Python 3.9
- Reuse of WebRTC `source_key`

## [2.6.0]
### Added
- Ability to pass `scheduled_start_time` equal to `null` in special cases
### Changed
- Validation of `title` and `description` parameters according to platforms limits
- Clients must sent `scheduled_start_time` on reusing upcoming broadcast

## [2.5.0]
### Added
- Method for getting video categories on Youtube
- Method for getting video on Youtube
- Additional parameters for Youtube broadcasts

## [2.4.0]
### Added
- Methods for starting and stopping WebRTC push to RTMP
- Method for getting scheduled broadcasts on Youtube
- Method for using scheduled broadcasts on Youtube

## [2.3.0]
### Added
- `token` parameter to `GET /auth/{platform}` method
### Changed
- Use `platforms` version 2.16.1

## [2.2.1]
### Changed
- Use `platforms` version 2.13.0

## [2.2.0]
### Changed
- Only one active broadcast is available
### Added
- Option to set privacy of broadcast

## [2.1.1]
### Fixed
- Increase scheduled time delta for Youtube broadcasts

## [2.1.0]
### Changed
- Default broadcasts not used any more. Every time new broadcast is created.

## [2.0.0]
### Remove
- Mixer support
### Changed
- Clickhouse table `events` renamed to `caster_events`

## [1.0.0]
### Changed
- New methods for gathering statistics
- Logging config moved to onlineconf
### Added
- Integration with Sentry

## [0.2.1]
### Fixed
- Update `title` and `description` if broadcast already exists

## [0.2.0]
### Added
- Optional `description` parameter for broadcasts on `Youtube`, `VK` and `OK`

## [0.1.8]
### Changed
- Use `platforms` version 0.0.13

## [0.1.7]
### Added
- Methods for gathering statistics on finished streams

## [0.1.6]
### Changed
- Use `da_auth` version 1.0.0

## [0.1.5]
### Changed
- Use separate `validators` module
- Use `da_auth` version 0.0.5

## [0.1.4]
### Changed
- Use separate `platforms` module

## [0.1.3]
### Fixed
- Fixed invalid handling of absent or invalid auth token

### Changed
- Use `asynctnt` version 1.1

## [0.1.2]
### Changed
- Use separate `da_auth` module
- Move `rtmp_uri` for Mixer to config
- Move domain for `share_uri` for Periscope to config

## [0.1.1]
### Fixed
Various bug fixes

## [0.1.0]
### Added
* Methods for managing broadcasts on:
    - Periscope
    - Twitch
    - YouTube
    - VK
    - OK
    - Mixer
* Method for authentication on _Donation Alerts_

[Unreleased]: https://gitlab.corp.mail.ru/myspb/casters/backend/compare/master...v2.22.0
[2.22.0]: https://gitlab.corp.mail.ru/myspb/casters/backend/compare/v2.22.0...v2.21.0
[2.21.0]: https://gitlab.corp.mail.ru/myspb/casters/backend/compare/v2.21.0...v2.20.0
[2.20.0]: https://gitlab.corp.mail.ru/myspb/casters/backend/compare/v2.20.0...v2.19.0
[2.19.0]: https://gitlab.corp.mail.ru/myspb/casters/backend/compare/v2.19.0...v2.18.0
[2.18.0]: https://gitlab.corp.mail.ru/myspb/casters/backend/compare/v2.18.0...v2.17.3
[2.17.3]: https://gitlab.corp.mail.ru/myspb/casters/backend/compare/v2.17.3...v2.17.2
[2.17.1]: https://gitlab.corp.mail.ru/myspb/casters/backend/compare/v2.17.1...v2.17.0
[2.17.0]: https://gitlab.corp.mail.ru/myspb/casters/backend/compare/v2.17.0...v2.16.1
[2.16.1]: https://gitlab.corp.mail.ru/myspb/casters/backend/compare/v2.16.1...v2.16.0
[2.16.0]: https://gitlab.corp.mail.ru/myspb/casters/backend/compare/v2.16.0...v2.15.0
[2.15.0]: https://gitlab.corp.mail.ru/myspb/casters/backend/compare/v2.15.0...v2.14.0
[2.14.0]: https://gitlab.corp.mail.ru/myspb/casters/backend/compare/v2.14.0...v2.13.0
[2.13.0]: https://gitlab.corp.mail.ru/myspb/casters/backend/compare/v2.13.0...v2.12.1
[2.12.1]: https://gitlab.corp.mail.ru/myspb/casters/backend/compare/v2.12.1...v2.12.0
[2.12.0]: https://gitlab.corp.mail.ru/myspb/casters/backend/compare/v2.12.0...v2.11.0
[2.11.0]: https://gitlab.corp.mail.ru/myspb/casters/backend/compare/v2.11.0...v2.10.1
[2.10.1]: https://gitlab.corp.mail.ru/myspb/casters/backend/compare/v2.10.1...v2.10.0
[2.10.0]: https://gitlab.corp.mail.ru/myspb/casters/backend/compare/v2.10.0...v2.9.1
[2.9.1]: https://gitlab.corp.mail.ru/myspb/casters/backend/compare/v2.9.1...v2.9.0
[2.9.0]: https://gitlab.corp.mail.ru/myspb/casters/backend/compare/v2.9.0...v2.8.0
[2.8.0]: https://gitlab.corp.mail.ru/myspb/casters/backend/compare/v2.8.0...v2.7.0
[2.7.0]: https://gitlab.corp.mail.ru/myspb/casters/backend/compare/v2.7.0...v2.6.0
[2.6.0]: https://gitlab.corp.mail.ru/myspb/casters/backend/compare/v2.6.0...v2.5.0
[2.5.0]: https://gitlab.corp.mail.ru/myspb/casters/backend/compare/v2.5.0...v2.4.0
[2.4.0]: https://gitlab.corp.mail.ru/myspb/casters/backend/compare/v2.4.0...v2.3.0
[2.3.0]: https://gitlab.corp.mail.ru/myspb/casters/backend/compare/v2.3.0...v2.2.1
[2.2.1]: https://gitlab.corp.mail.ru/myspb/casters/backend/compare/v2.2.1...v2.2.0
[2.2.0]: https://gitlab.corp.mail.ru/myspb/casters/backend/compare/v2.2.0...v2.1.1
[2.1.1]: https://gitlab.corp.mail.ru/myspb/casters/backend/compare/v2.1.1...v2.1.0
[2.1.0]: https://gitlab.corp.mail.ru/myspb/casters/backend/compare/v2.1.0...v2.0.0
[2.0.0]: https://gitlab.corp.mail.ru/myspb/casters/backend/compare/v2.0.0...v1.0.0
[1.0.0]: https://gitlab.corp.mail.ru/myspb/casters/backend/compare/v1.0.0...v0.2.1
[0.2.1]: https://gitlab.corp.mail.ru/myspb/casters/backend/compare/v0.2.1...v0.2.0
[0.2.0]: https://gitlab.corp.mail.ru/myspb/casters/backend/compare/v0.2.0...v0.1.8
[0.1.8]: https://gitlab.corp.mail.ru/myspb/casters/backend/compare/v0.1.8...v0.1.7
[0.1.7]: https://gitlab.corp.mail.ru/myspb/casters/backend/compare/v0.1.7...v0.1.6
[0.1.6]: https://gitlab.corp.mail.ru/myspb/casters/backend/compare/v0.1.6...v0.1.5
[0.1.5]: https://gitlab.corp.mail.ru/myspb/casters/backend/compare/v0.1.5...v0.1.4
[0.1.4]: https://gitlab.corp.mail.ru/myspb/casters/backend/compare/v0.1.4...v0.1.3
[0.1.3]: https://gitlab.corp.mail.ru/myspb/casters/backend/compare/v0.1.3...v0.1.2
[0.1.2]: https://gitlab.corp.mail.ru/myspb/casters/backend/compare/v0.1.2...v0.1.1
[0.1.1]: https://gitlab.corp.mail.ru/myspb/casters/backend/compare/v0.1.1...v0.1.0
[0.1.0]: https://gitlab.corp.mail.ru/myspb/casters/backend/tree/75ecff0c
