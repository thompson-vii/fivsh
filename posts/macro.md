---
title: Guide to macro 
description: 
date: 2023-07-20
tags:
  - Automation
  - Autohotkey
layout: layouts/post.njk
---

# Macros

Macros can fire key stroke sequences, map several key combinations to a single key press. Depend on what software/hardware solution you use, they can also execute mouse movements, remap MIDI commands and do other fancy shit. 

Macros are useful for:
 - Executing repetitive or very long actions
 - Rearrange keymappings
 - There are more, probably. 



## Software Based Solutions
Requires no hardware modification. Remapping is active as long as the program is running. Some tools are Windows only, others are cross platform. 

Some software also provide ways to record macros automations:
[Quick start: Create a macro - Microsoft Support](https://support.microsoft.com/en-us/office/quick-start-create-a-macro-741130ca-080d-49f5-9471-1e5fb3d581a8) [Map - Neovim docs](https://neovim.io/doc/user/map.html) 




## Hardware Based Solutions 

Early on there are already [keyboards with programmable functions built in onto themselves](https://youtu.be/6CM4ejSdbHc?t=73), tho rather primitive (remapping key, replay recorded key sequences)

More recent keyboards (that you can still buy) will require running some software on the host. [POS - Cherry](https://www.cherryamericas.com/applications/pos)

Some of them command a price premium over their standard counterparts [Genovation Programmable Keypads & Keyboards](https://www.genovation.com/product-category/programmables/) 

Some configuration software only runs on Windows. I guess Mouse with multiple buttons also fall under this category...

In the custom keyboard niche there are boards running on QMK and its derivatives. Originally only configurable via code but GUI like Via and Vial made it more accessible to the general audience. Layout varies greatly with many customizing options available from different vendors. 

Dedicated Hardware that only works with specific applications doesn't count cause they can't be repurposed for other task. 

They work everywhere once configured but between Windows, Linux, MacOS. Special keys need to be programmed for each platform. 

# Feature Table
|  | Win | Linux | MacOs | Require specialized hardware | Has GUI | Controls mouse | Active development |
| --- | ---| ---| --- | --- | --- | --- | --- | 
| AutoHotkey | Yes | - | - | - | - | Yes | Yes |
| Hid Macros¹ | Yes | - | - | -| Yes | - | No |
| LuaMacros¹ | Yes | - | - | - | - | - | No |
| Kmonad | Yes | Yes | Yes | - | - | - | Yes |
| Kanata | Yes | Yes | - | - | - | Yes | Yes |
| QMK/ZMK/KMK | Yes | Yes | Yes | Yes | Yes² | Yes³ | Yes |
| SteamInput | Yes | Yes | Yes | Yes⁴ | Yes | Yes | Yes |
| Autohotpie | Yes | - | - | No | Yes | Yes | Yes |

[1]: Can have different mapping for multiple keyboards, but require intercepting drivers.

[2]: The firmware must be compiled with via / vial support.

[3]: The firmware must be compiled with MOUSEKEY support. 

[4]: Supports Game controller from: Xbox1, PlayStation, Nintendo Switch, Steam controller.

# Software Based Macros

## AutoHotkey

Windows only, as it uses OS specific APIs. Beside key press and mouse remapping capabilities, Autohotkey can substitute key sequences, run commands. It has a mini programming language for more sophisticated behaviors, can be used to author GUI utilities, and other features I have not used myself. 

Autohotkey comes with two version. Beginning on 2023 V1 is considered legacy. V1 and V2 scripts are not compatible, though V1 will still work and bug fixes are still been made. 

There are several macro programs that are based on Autohotkey. 

/r/AutoHotkey | [AutoHotkey Discord](https://discord.com/invite/Aat7KHmG7v)

## Hid Macros

The program is no longer maintained by the original dev. 

I have not used it. 

[HID macros](https://www.hidmacros.eu/whatisit.php) 

## LuaMacros

The program is also no longer maintained. 

[LuaMacros Github Repo](https://github.com/me2d13/luamacros)

## Kmonad

Infrequent update due to dev's health issue. 

[Kmonad Github Repo](https://github.com/kmonad/kmonad)

## Kanata

Inspired by kmonad, the features are mostly similar with some differences. Written in rust. No MacOs support.

[Kanata Github Repo](https://github.com/jtroo/kanata)

## SteamInput via GlosSI

This is a weird one that uses steamInput to remap keys, which requires running steam and a controller. SteamInput supports keyboard and mouse actions. 

The configuration is done through the configuration application that ships with steam. The controller must be on for configuration.

Support controller: switch pro, Xbox controller, PlayStation DualShock, steam controller.

There is a desktop mapping which is always active whenever you are not running a game. SteamInput will switch to a different mapping when a steam game window is focused. 

GlosSI provides one click solution for adding applications into steam. It also provides a hooked steam overlay so custom GUI element like the radial menu and grid menu will also work, but the application must be launched from steam's big picture mode, which is awkward and makes the screen flash black for a moment. 

See SteamController's [wiki](https://www.reddit.com/r/SteamController/wiki/getting-started/) for guide on how to setup the configuration.

/r/SteamController | [GlosSI Repo](https://github.com/Alia5/GlosSI) | 

### Autohotpie

A recent discovery thanks to a friend. I have not use it much yet but it looks promising. 

Based on Autohotkey. 

# Hardware Based Solutions

### QMK/ZMK/KMK supported Keyboard

Special firmware used by mostly custom keyboards. Once loaded the keyboard will work anywhere. 

The firmware is provide in a hex file. Most vendor provides a working out of box firmware that might have via / vial support, which is a gui interface for configuring the keyboard. The compiled firmware need to have mousekey enabled to use mouse inputs. 


https://qmk.fm/ | [QMK Github Repo](https://github.com/qmk/qmk_firmware) | /r/olkb | [QMK Discord](https://discord.com/invite/Uq7gcHh)

### Midi Controller

[MIDIControl for obs](https://obsproject.com/forum/resources/midicontrol-control-obs-soundboard-twitch-chat-with-midi-devices.940/)

[AutoHotkey midi to macro](https://github.com/laurence-myers/midi-to-macro)

[Midikey2Key](https://midikey2key.de/)

[Bome midi translator Classic](https://www.bome.com/shop/bome-midi-translator-classic)

Maps midi to keyboard and mouse input. 


# Specific Problems

### F13 to F24

The majority of keyboards available today only have F1 to F12. Support for F13 to F24 is inconsistent. Windows and Linux both support F13 to F24. MacOs only supports up to F19. Support for the extra functions keys also vary between different programs.

There is little to no chance shortcut assigned with those keys conflicts with any existing applications.

[QMK keycode reference](https://github.com/qmk/qmk_firmware/blob/master/docs/keycodes.md)

### Shift + Keypad on Windows

[Microsoft Devblogs](https://devblogs.microsoft.com/oldnewthing/20040906-00/?p=37953)

> If NumLock is on (as it usually is), then pressing a key on the numeric keypad while holding the shift key overrides NumLock and instead generates the arrow key (or other navigation key) printed in small print under the big digits. 

When using macro involving shift key in kmonad/kanata, toggle the numlock before and after the shortcut.

Linux by default does not have such behavior, if you need the keypad for mapping, [check if microsoft numpad compatibility is enabled on your DE](https://askubuntu.com/questions/57079/xubuntu-make-shiftnumpad-work-like-windows)



# Useful links

/r/macro_pads cataloging macro pads