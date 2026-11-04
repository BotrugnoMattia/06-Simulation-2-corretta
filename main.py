from laboratorio import LaboratorioBiotecnologico
from test_biologico import TestBiologico


def main() -> None:
    laboratorio = LaboratorioBiotecnologico("BioLab - controllo qualita")
    test_esempio = [
        TestBiologico("QC-01", "BIO-24A", "endotossine", 0.8, 1.0, "EU/mL"),
        TestBiologico("QC-02", "BIO-24A", "DNA residuo", 4.2, 10.0, "ng/mL"),
        TestBiologico("QC-03", "BIO-24B", "carica microbica", 120, 100, "CFU/mL"),
        TestBiologico("QC-04", "BIO-24B", "endotossine", 1.0, 1.0, "EU/mL"),
        TestBiologico("QC-05", "BIO-24C", "DNA residuo", 12, 10.0, "ng/mL"),
    ]

    for test in test_esempio:
        laboratorio.registra_test(test)

    laboratorio.riepilogo()

    campione_da_cercare = "BIO-24A"
    test_campione = laboratorio.cerca_per_campione(campione_da_cercare)
    if test_campione:
        print("Test del campione", campione_da_cercare)
        for test in test_campione:
            print(test.codice, test.parametro, laboratorio.esiti[test.codice])
    else:
        print("Nessun test trovato per il campione", campione_da_cercare)

    try:
        laboratorio.registra_test(test_esempio[0])
    except ValueError as errore:
        print("Impossibile registrare il test:", errore)

    campione_inesistente = "BIO-99Z"
    if not laboratorio.cerca_per_campione(campione_inesistente):
        print("Nessun test trovato per il campione", campione_inesistente)


if __name__ == "__main__":
    main()