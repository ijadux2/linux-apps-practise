{ config, pkgs, home-manager, ... }:

{
  programs.kitty = {
    enable = true;
    theme = "catppuccin-mocha";
    font-family = "JetBrains Mono";
    font-size = "18";
    comfirm-os-close;
    tab-size = "2";
    #etc
  };

  programs.neovim = {
    enable = true;
    support.lua.config.enable = true;
    support.config.nvimDirectory = "/home/ijadux2/.config/nvim/"
    plugins = {
      treesitter.enable = true;
      catppuccin-mocha.theme.enable = true;
      lazy.enable = true;
    }; 
    language.support = {
     "lua"
     "nix"
     "css"
    "html"
    "javascript"
    };
  };

  programs.chromium.enable = true;
  
  programs.zsh = {
    enable = true;
          OhMyZsh = {
      enable = true;
      theme = "mh";
      plugins = [ "git" "sudo" "zoxide" "zsh-syntaxhighlighting"];
    };
     ShellAliasses = {
      cd = "z";
      ls = "lsd";
      lt = "ls --tree";
      x = "clear";
    };
    PROMPT = "%B%F{green}[%n@Nix-devops:%~]$ %f%b";
  };
  

  programs.home-manager = {
    enable = true;
    home.Packages = with pkgs; [
      kitty
      zsh
      chromium
      neovim
    ];

    home.file =  {
    };

    home.homeDirectory = "/home/ijadux2/";
    home.homeUser = "ijadux2";


  };
}
