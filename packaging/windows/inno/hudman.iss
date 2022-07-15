; SPDX-FileCopyrightText: 2016-2022 EasyCoding Team
;
; SPDX-License-Identifier: GPL-3.0-or-later

#define VERSION GetVersionNumbersString("..\results\dist\hudman.exe")
#define BASEDIR "..\results\dist"

#if GetEnv('CI_HASH') == ''
#define _RELEASE 1
#endif

[Setup]
AppId={{BE200E8E-42D0-493E-9BAA-97A7DC741E56}
AppName=HUD Manager
AppVerName=HUD Manager
AppPublisher=EasyCoding Team
AppPublisherURL=https://www.easycoding.org/
AppVersion={#VERSION}
AppSupportURL=https://github.com/xvitaly/hudman/issues
AppUpdatesURL=https://github.com/xvitaly/hudman/releases
DefaultDirName={localappdata}\HUD Manager
DefaultGroupName=HUD Manager
AllowNoIcons=yes
LicenseFile=..\..\..\LICENSE
OutputDir=..\results
OutputBaseFilename={#GetEnv('PREFIX')}_setup
SetupIconFile=..\assets\hudman.ico
UninstallDisplayIcon={app}\hudman.exe
Compression=lzma2
SolidCompression=yes
PrivilegesRequired=lowest
PrivilegesRequiredOverridesAllowed=commandline
ShowLanguageDialog=auto
ArchitecturesAllowed=x64
ArchitecturesInstallIn64BitMode=x64
MinVersion=6.1sp1
ChangesEnvironment=yes
VersionInfoVersion={#VERSION}
VersionInfoDescription=HUD Manager
VersionInfoCopyright=(c) 2016-2022 EasyCoding Team. All rights reserved.
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
Name: "core"; Description: "{cm:ComponentCoreDescription}"; Types: standard system nokeys; Flags: fixed
Name: "apikey"; Description: "{cm:ComponentAPIKeySubDescription}"; Types: standard system nokeys; Flags: exclusive
Name: "apikey\sysenv"; Description: "{cm:ComponentAPIKeySysEnvDescription}"; Types: system; Flags: exclusive
Name: "apikey\launcher"; Description: "{cm:ComponentAPIKeyLauncherDescription}"; Types: standard; Flags: exclusive
Name: "apikey\nokeys"; Description: "{cm:ComponentAPIKeyNoKeyDescription}"; Types: nokeys; Flags: exclusive

[Files]
Source: "{#BASEDIR}\hudman.exe"; DestDir: "{app}"; Flags: ignoreversion; Components: core
Source: "{tmp}\hudmanc.cmd"; DestDir: "{app}"; Flags: external; Components: apikey\launcher

#ifdef _RELEASE
Source: "{#BASEDIR}\hudman.exe.sig"; DestDir: "{app}"; Flags: ignoreversion; Components: core
#endif

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
    Result := (Length(GetAPILoginInternal()) < 4) or (Length(GetAPIKeyInternal()) < 10)
end;

function IsKeylessInstallation(): Boolean;
begin
    Result := WizardIsComponentSelected('apikey\nokeys')
end;

function GenerateLauncher(FileName: String): Boolean;
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
                    Result := GenerateLauncher(ExpandConstant('{tmp}\hudmanc.cmd'));
                end
        end
    else
        begin
            Result := True
        end
end;
