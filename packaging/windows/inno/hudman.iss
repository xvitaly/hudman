﻿; SPDX-FileCopyrightText: 2016-2021 EasyCoding Team
;
; SPDX-License-Identifier: GPL-3.0-or-later

#define VERSION GetFileVersion("..\results\dist\hudman.exe")
#define BASEDIR "..\results\dist"
#define CI_COMMIT GetEnv('CI_HASH')
#if CI_COMMIT == ''
#define _RELEASE 1
#endif

[Setup]
AppId={{67B50FB5-DEAE-4933-A1DE-4946879B879F}
AppName=HUD Manager
AppVerName=HUD Manager
AppPublisher=EasyCoding Team
AppPublisherURL=https://www.easycoding.org/
AppVersion={#VERSION}
AppSupportURL=https://github.com/xvitaly/hudman/issues
AppUpdatesURL=https://github.com/xvitaly/hudman/releases
DefaultDirName={localappdata}\hudman
DefaultGroupName=HUD Manager
AllowNoIcons=yes
LicenseFile=..\..\..\LICENSE
OutputDir=..\results
#ifdef _RELEASE
OutputBaseFilename=hudman_{#GetEnv('RELVER')}
#else
OutputBaseFilename=snapshot_{#CI_COMMIT}
#endif
SetupIconFile=..\assets\hudman.ico
UninstallDisplayIcon={app}\hudman.exe
Compression=lzma2
SolidCompression=yes
PrivilegesRequired=lowest
PrivilegesRequiredOverridesAllowed=commandline
ShowLanguageDialog=auto
ArchitecturesAllowed=x64
ArchitecturesInstallIn64BitMode=x64
MinVersion=6.1.7601
VersionInfoVersion={#VERSION}
VersionInfoDescription=HUD Manager
VersionInfoCopyright=(c) 2005-2020 EasyCoding Team. All rights reserved.
VersionInfoCompany=EasyCoding Team

[Messages]
BeveledLabel=EasyCoding Team

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl,locale\en\cm.isl"; InfoBeforeFile: "locale\en\readme.txt"
Name: "russian"; MessagesFile: "compiler:Languages\Russian.isl,locale\ru\cm.isl"; InfoBeforeFile: "locale\ru\readme.txt"

[Types]
Name: standard; Description: "{cm:TypeStandardDescription}"
Name: system; Description: "{cm:TypeSystemDescription}"
Name: nokeys; Description: "{cm:TypeNoKeysDescription}"

[Components]
Name: "core"; Description: "{cm:ComponentCoreDescription}"; Types: standard system; Flags: fixed
Name: "apikey"; Description: "{cm:ComponentAPIKeySubDescription}"; Types: standard system; Flags: exclusive
Name: "apikey\sysenv"; Description: "{cm:ComponentAPIKeySysEnvDescription}"; Types: system; Flags: exclusive restart
Name: "apikey\launcher"; Description: "{cm:ComponentAPIKeyLauncherDescription}"; Types: standard; Flags: exclusive
Name: "apikey\nokeys"; Description: "{cm:ComponentAPIKeyNoKeyDescription}"; Types: nokeys; Flags: exclusive

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"

[Files]
Source: "{#BASEDIR}\hudman.exe"; DestDir: "{app}"; Flags: ignoreversion; Components: core
Source: "{tmp}\hudmanc.cmd"; DestDir: "{app}"; Flags: external; Components: apikey\launcher

#ifdef _RELEASE
Source: "{#BASEDIR}\hudman.exe.sig"; DestDir: "{app}"; Flags: ignoreversion; Components: core
#endif

[Icons]
Name: "{group}\HUD Manager"; Filename: "{app}\hudman.exe"; Components: "apikey\sysenv or apikey\nokeys"
Name: "{group}\HUD Manager"; Filename: "{app}\hudmanc.cmd"; IconFilename: "{app}\hudman.exe"; Components: "apikey\launcher"
Name: "{group}\{cm:ProgramOnTheWeb,HUD Manager}"; Filename: "https://github.com/xvitaly/hudman"; Components: core
Name: "{userdesktop}\HUD Manager"; Filename: "{app}\hudman.exe"; Components: "apikey\sysenv or apikey\nokeys"; Tasks: desktopicon
Name: "{userdesktop}\HUD Manager"; Filename: "{app}\hudmanc.cmd"; IconFilename: "{app}\hudman.exe"; Components: "apikey\launcher"; Tasks: desktopicon

[Registry]
Root: HKCU; Subkey: "Environment"; ValueType: string; ValueName: "HUDMAN_LOGIN"; ValueData: "{code:GetAPILogin}"; Flags: uninsdeletevalue; Components: "apikey\sysenv"
Root: HKCU; Subkey: "Environment"; ValueType: string; ValueName: "HUDMAN_APIKEY"; ValueData: "{code:GetAPIKey}"; Flags: uninsdeletevalue; Components: "apikey\sysenv"

[Code]
var
    APIKeyPage: TInputQueryWizardPage;

procedure AddAPIKeyPage();
begin
    APIKeyPage := CreateInputQueryPage(wpSelectTasks, CustomMessage('APIKeyPageCaption'), CustomMessage('APIKeyPageDescription'), CustomMessage('APIKeyPageAdditionalText'));
    APIKeyPage.Add(CustomMessage('APIKeyPageInputFieldLoginText'), False)
    APIKeyPage.Add(CustomMessage('APIKeyPageInputFieldTokenText'), False)
end;

procedure InitializeWizard();
begin
    AddAPIKeyPage()
end;

function GetAPILoginInternal(): String;
begin
    Result := APIKeyPage.Values[0]
end;

function GetAPILogin(Value: String): String;
begin
    Result := GetAPILoginInternal()
end;

function GetAPIKeyInternal(): String;
begin
    Result := APIKeyPage.Values[1]
end;

function GetAPIKey(Value: String): String;
begin
    Result := GetAPIKeyInternal()
end;

function VerifyAPICredentials(): Boolean;
begin
    Result := (Length(GetAPILoginInternal()) < 4) and (Length(GetAPIKeyInternal()) < 10)
end;

function IsKeylessInstallation(): Boolean;
begin
    Result := WizardIsComponentSelected('apikey\nokeys')
end;

function GenerateBotLauncher(FileName: String): Boolean;
var
    Contents: TArrayOfString;
begin
    SetArrayLength(Contents, 7);
    Contents[0] := '@echo off';
    Contents[1] := '';
    Contents[2] := 'title HUD Manager';
    Contents[3] := 'set HUDMAN_LOGIN=' + GetAPILoginInternal();
    Contents[4] := 'set HUDMAN_APIKEY=' + GetAPIKeyInternal();
    Contents[5] := '';
    Contents[6] := '.\hudman.exe %*';
    Result := SaveStringsToFile(FileName, Contents, False)
end;

function ShouldSkipPage(CurPageID: Integer): Boolean;
begin
    if CurPageID = APIKeyPage.ID then
        begin
            Result := IsKeylessInstallation()
        end
    else
        begin
            Result := False
        end
end;

function NextButtonClick(CurPageID: Integer): Boolean;
begin
    if CurPageID = APIKeyPage.ID then
        begin
            if (VerifyAPICredentials()) then
                begin
                    MsgBox(CustomMessage('APIKeyPageErrorMessage'), mbError, MB_OK);
                    Result := False
                end
            else
                begin
                    Result := GenerateBotLauncher(ExpandConstant('{tmp}\hudmanc.cmd'));
                end
        end
    else
        begin
            Result := True
        end
end;
