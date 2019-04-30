package serverCentrale;

import java.util.ArrayList;

import eccezioni.InvioOrdineRIdondanteException;
import eccezioni.NessunProdottoException;
import ordinazioni.Ordinazione;
import ordinazioni.StatoOrdinazione;
import prodotti.Prodotto;

public interface ServerCentraleInterface
{
    public Ordinazione creaOrdinazione(int idTavolo);
    public float getConto(int idTavolo);
    public boolean inviaOrdine(String idOrdinazione) throws NessunProdottoException, InvioOrdineRIdondanteException;
    public ArrayList<Ordinazione> getOrdiniInviati();
    public boolean eleminaOrdinazione(String idOrdinazione);
    public void aggiungiProdottoMenu(Prodotto prodotto);
    public void aggiungiProdottoOrdinazine(String idOrdinazione, Prodotto prodotto, int quantita);
    public StatoOrdinazione getStatoOrdinazione(String idOrdinazione);
}
