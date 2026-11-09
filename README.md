# Opera Magna · atlas-nebelungenring

Experiencias web en torno a las grandes obras. Primera sala: **El Anillo del Nibelungo** (Wagner, *Der Ring des Nibelungen*).

- Web: https://opera-magna.web.app/ · la obra en https://opera-magna.web.app/anillo/
- Firebase: proyecto `opera-magna` (cuenta mirrorshades.noe@gmail.com)

## Estructura

```
public/                 lo que se publica
  index.html            entrada de Opera Magna (lista de obras)
  404.html
  anillo/index.html     El Anillo, archivo único generado (no editar a mano)
src/anillo/
  ring.src.html         fuente de la página
  build.py              genera public/anillo/index.html
  data/                 mapa (Natural Earth), láminas Rackham/Hendrich, leitmotive
  vendor/               three.js r128 y tipografías (OFL), incrustadas al construir
firebase.json           alojamiento y cabeceras de seguridad (CSP sin terceros)
.github/workflows/      publicación manual en Firebase
```

Construir: `python3 src/anillo/build.py`

## Publicar desde GitHub (sin instalar nada)

Configuración, una sola vez:

1. Abre https://console.cloud.google.com/iam-admin/serviceaccounts?project=opera-magna (con mirrorshades.noe@gmail.com).
2. **Crear cuenta de servicio** → nombre `github-deploy` → función **Firebase Hosting Admin** (y **API Keys Viewer**) → Listo.
3. En la cuenta creada: **Claves → Agregar clave → Crear clave nueva → JSON**. Se descarga un archivo.
4. En GitHub: este repositorio → **Settings → Secrets and variables → Actions → New repository secret**.
   - Nombre: `FIREBASE_SERVICE_ACCOUNT_OPERA_MAGNA`
   - Valor: pega el contenido completo del JSON.
5. Borra el JSON descargado de tu ordenador.

Cada publicación:

**Actions → Publicar en Firebase → Run workflow** → elige `preview` (prueba, 7 días) o `live` (web pública).

Nada se publica solo: el flujo únicamente se ejecuta a mano.

## Publicar desde tu ordenador (alternativa)

```bash
npm install -g firebase-tools
firebase login
firebase deploy --only hosting
```

## Añadir otra obra

1. `public/<obra>/index.html` (y sus fuentes en `src/<obra>/`).
2. Una línea en la lista `.works` de `public/index.html`.
3. Publicar.

## Créditos y derechos

Láminas de Arthur Rackham (1867–1939) y Hermann Hendrich (1854–1931), dominio público. Mapa: Natural Earth (dominio público). Leitmotive: Wagner Ring Dataset (CC BY 3.0). Tipografías: SIL Open Font License. three.js: MIT. Texto y diseño: Dear · contenido elaborado con asistencia de IA bajo dirección editorial humana.
