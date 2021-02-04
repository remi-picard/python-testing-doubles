# Présentation Python Testing Doubles

## Slides / Deck

### Installation

- [Install Ruby and Gem](https://rubyinstaller.org/)
- Install bundler :

```bash
gem install bundler
```

- Install the dependencies :

```bash
# bundle config --local github.https true
# bundle --path=.bundle/gems --binstubs=.bundle/.bin
bundle install
```

- Get RevealJS

```bash
git clone -b 3.6.0 --depth 1 https://github.com/hakimel/reveal.js.git
```

- Generate presentation

```
bundle exec asciidoctor-revealjs presentation.adoc
```

## PDF

### Installation

http://asciidoctor.org/docs/asciidoctor-pdf/

```
gem install asciidoctor-pdf --pre
gem install coderay
```

### Génération

- Remplacer l'entête revealjs de presentation.adoc par :

```
Rémi PICARD <picard.remi@gmail.com>
:doctype: book
:reproducible:
:source-highlighter: coderay
:listing-caption: Listing
:pdf-page-size: Letter

Git Flow - Un standard pour votre gestion de configuration
```

- Générer avec `asciidoctor-pdf presentation.adoc`
